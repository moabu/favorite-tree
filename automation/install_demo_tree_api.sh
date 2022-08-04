#!/bin/bash
set -eo pipefail
TREE_FQDN=$1
TREE_CI_CD_RUN=$2
EXT_IP=$3
INSTALL_ISTIO=$4
HACK=$5

if [[ ! "$TREE_FQDN" ]]; then
  read -rp "Enter Hostname [my.ecosia.org]:                           " TREE_FQDN
fi
if ! [[ $TREE_FQDN == *"."*"."* ]]; then
  echo "[E] Hostname provided is invalid or empty.
    Please enter a FQDN with the format my.ecosia.org"
  exit 1
fi

if [[ -z $EXT_IP ]]; then
  EXT_IP=$(dig +short myip.opendns.com @resolver1.opendns.com)
fi

if [[ -z $HACK ]]; then
  HACK=false
fi

sudo apt-get update
sudo apt-get install python3-pip -y
sudo pip3 install pip --upgrade
sudo pip3 install setuptools --upgrade
sudo pip3 install pyOpenSSL --upgrade
sudo apt-get update
sudo apt-get install build-essential unzip -y
sudo pip3 install requests --upgrade
sudo pip3 install shiv
sudo snap install microk8s --classic
sudo microk8s.status --wait-ready
sudo microk8s.enable dns registry ingress storage
sudo microk8s kubectl get daemonset.apps/nginx-ingress-microk8s-controller -n ingress -o yaml | sed -s "s@ingress-class=public@ingress-class=nginx@g" | microk8s kubectl apply -f -
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install net-tools
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo microk8s config | sudo tee ~/.kube/config > /dev/null
sudo snap alias microk8s.kubectl kubectl

docker build ./api --file ./api/Dockerfile --tag localbuild/tree:latest
docker image save localbuild/tree:latest  > image.tar
microk8s.ctr image import image.tar

KUBECONFIG=~/.kube/config
sudo microk8s.kubectl create namespace tree-api --kubeconfig="$KUBECONFIG" || echo "namespace exists"

if [[ $INSTALL_ISTIO == "true" ]]; then
  sudo microk8s.kubectl label ns tree-api istio-injection=enabled
  sudo curl -L https://istio.io/downloadIstio | sh -
  cd istio-*
  export PATH=$PWD/bin:$PATH
  sudo ./bin/istioctl install --set profile=demo -y
  cd ..
fi

sudo helm repo add bitnami https://charts.bitnami.com/bitnami
sudo microk8s.kubectl get po --kubeconfig="$KUBECONFIG"
sudo helm install my-release --set auth.rootPassword=Test1234#,auth.database=tree bitnami/mysql -n tree-api --kubeconfig="$KUBECONFIG"

echo "$EXT_IP $TREE_FQDN" | sudo tee -a /etc/hosts > /dev/null
cat << EOF >> override.yaml
tree-api:
  image:
    pullPolicy: IfNotPresent
    repository: localbuild/tree
    tag: latest
  testEnviroment: true
  ingress:
    istio:
      enabled: $INSTALL_ISTIO
    nginx:
      ingresClass: nginx
      enabled: true
    path: /
    hosts:
      - $TREE_FQDN
    tls:
      - secretName: tls-certificate
        hosts:
          - $TREE_FQDN
  hack:
    enabled: $HACK
    favoriteTree: Olive Tree
EOF
sudo helm install tree-api ./chart/tree -n tree-api -f override.yaml --kubeconfig="$KUBECONFIG"
echo "Waiting for tree api to come up. This may take 5-10 mins....Please do not cancel out...This will wait for the tree api to be ready.."
sleep 300
cat << EOF > testendpoints.sh
sudo microk8s config > config
KUBECONFIG="$PWD"/config
sleep 10
echo -e "Testing tree endpoint.. \n"
curl -k https://$TREE_FQDN/tree
cd ..
EOF
sudo microk8s.kubectl get deploy -n tree-api --kubeconfig="$KUBECONFIG"
sleep 10
sudo microk8s.kubectl describe deploy tree-api -n tree-api --kubeconfig="$KUBECONFIG"
echo "mysql+pymysql://root:Test1234#@my-release-mysql.tree-api.svc:3306/tree?charset=utf8" > uri
sudo microk8s.kubectl create secret generic sql-secret-uri --from-file=uri -n tree-api --kubeconfig="$KUBECONFIG"
sudo microk8s.kubectl -n tree-api wait --for=condition=available --timeout=300s deploy/tree-api --kubeconfig="$KUBECONFIG" || echo "Couldn't find deployment running tests anyways..."
sudo bash testendpoints.sh
echo -e "You may re-execute bash testendpoints.sh to do a quick test to check the tree endpoint."
