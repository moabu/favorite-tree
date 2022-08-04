# My Favorite Tree API

This project aims to serve a simple API using Flask that fetches the favorite tree of the user. This can further expand into more operations such as creating and deleting a favorite tree.

##  Run locally

```bash
export ENV FLASK_APP=main.core:app FLASK_ENV=development SQLALCHEMY_DATABASE_URI_FILEPATH=$HOME/sql_uri.txt
poetry run flask db upgrade
poetry run flask seed run --root=main/seeds
poetry run flask run
```

## Run on Docker

### Pre-requisite
- Latest Docker
- MySQL installed and prepared with access to db name, user, and password.
   
   ```bash
   echo"mysql+pymysql://<USER>:<PASSWORD>@db:3306/favorite_tree?charset=utf8" > $HOME/sql_uri.txt
   ```

```bash
docker build -t $USER/tree:dev .
docker run --rm -e SQLALCHEMY_DATABASE_URI_FILEPATH="/home/web/sql_uri.txt" -v $HOME/sql_uri.txt:/home/web/sql_uri.txt -p 5000:5000 -t $USER/tree:dev
```

## Run using Docker Compose
- Latest Docker

```bash
mkdir secrets
openssl rand -out secrets/db_root_password.txt -base64 12
openssl rand -out secrets/db_user_password.txt -base64 12
PASSWORD=$(<secrets/db_user_password.txt)
echo "mysql+pymysql://developer:$PASSWORD@db:3306/favorite_tree?charset=utf8" > secrets/sql_uri.txt
docker compose up --build -d
```

## Run using Helm

### Prerequisites
- MySQL installed and prepared with access to db name, user, and password.

   ```bash
   echo "mysql+pymysql://<USER>:<PASSWORD>@db:3306/favorite_tree?charset=utf8" > $HOME/uri
   ```
1. Modify or build out your custom [`values.yaml`](../chart/tree/README.md).
2. Create `tree-api` namespace `kubectl create ns tree-api`.
3. Create secret called `kubectl create secret generic sql-secret-uri --from-file=uri -n tree-api`
4. Install using `helm install tree-api ../chart/tree -n tree-api`

## Test

### Docker

```bash
curl  http://0.0.0.0:5000/tree -o fav_tree.json
```

### Kubernetes

```bash
#$TREE_DOMAIN is the `host` value inside the values.yaml used to during the helm install.
# You would need to map your local to the host
curl -k https://$TREE_DOMAIN/tree
```

Expected output on a fresh setup should be:


```json
 {
  "data": {
    "favorite": "Olive Tree", 
    "name": "Mohammad Abudayyeh", 
    "slug": "olive-tree"
  }
}
```

## Generate the Swagger file

```bash
poetry run flask openapi write --format=json favorite-tree-api.json
```

or if deployed got to

```bash
http://0.0.0.0:5000/api/swagger-ui 
```

## View the Swagger file

1. Open https://editor.swagger.io/
2. Copy the contents of the `favorite-tree-swagger-api.json`