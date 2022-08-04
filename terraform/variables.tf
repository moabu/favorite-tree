# ---------------------------------------------------------------------------------------------------------------------
# REQUIRED PARAMETERS
# These variables are expected to be passed in by the operator.
# ---------------------------------------------------------------------------------------------------------------------
# main.tf --> GET CREDS FOR EKS ACCESS

# cert-manager.tf -->  LAUNCH CERT MANAGER IN HA ON EKS IN AWS
variable "cert_manager_version" {
  type        = string
  description = "Cert Manager Version"
  default     = "1.8.0"
}
# tree.tf -->  LAUNCH CERT MANAGER ISSUER AND TREE API IN HA ON EKS IN AWS
