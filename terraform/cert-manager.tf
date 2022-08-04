# ---------------------------------------------------------------------------------------------------------------------
# LAUNCH CERT MANAGER IN HA ON AWS in EKS
# Design detailed in attached README.md
# ---------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# INSTALL CERTMANAGER RELEASE IN NAMESPACE
# ----------------------------------------------------------------------------------------------------------------------

resource "helm_release" "cert-manager" {
  name       = "cert-manager"
  repository = "https://charts.jetstack.io"
  chart      = "cert-manager"
  version    = var.cert_manager_version
  namespace  = "cert-manager"

  set {
    name  = "installCRDs"
    value = true
  }
  create_namespace = true
}
