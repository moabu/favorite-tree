# ---------------------------------------------------------------------------------------------------------------------
# LAUNCH FAVORITE TREE API IN HA ON EKS IN AWS
# Design detailed in attached README.md
# ---------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# INSTALL CERTMANAGER ISSUER IN TREE API NAMESPACE
# https://cert-manager.io/docs/faq/cluster-resource/
# ----------------------------------------------------------------------------------------------------------------------

resource "helm_release" "tree-cert-manager-issuer" {
  name      = "tree-cert-manager-issuer"
  chart     = "../charts/tree-cert-manager-issuer"
  namespace = "tree-api"
  depends_on = [helm_release.cert-manager]
}

# ----------------------------------------------------------------------------------------------------------------------
# INSTALL TREE API IN TREE API NAMESPACE
# ----------------------------------------------------------------------------------------------------------------------

resource "helm_release" "tree-cert-manager-issuer" {
  name      = "tree-api"
  chart     = "../charts/tree"
  namespace = "tree-api"
  depends_on = [helm_release.cert-manager]
}
