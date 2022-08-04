# ---------------------------------------------------------------------------------------------------------------------
# PREPARATION FOR EXECUTING ON EKS
# ---------------------------------------------------------------------------------------------------------------------

terraform {
  # This module is now only being tested with Terraform 1.0.x. However, to make upgrading easier, we are setting
  # 0.12.26 as the minimum version, as that version added support for required_providers with source URLs, making it
  # forwards compatible with 1.0.x code.
  required_version = ">= 0.12.26"
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "2.4.1"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.7.1"
    }
  }
}

# Use a random suffix to prevent overlap in network names
resource "random_string" "suffix" {
  length  = 4
  special = false
  upper   = false
}


# ----------------------------------------------------------------------------------------------------------------------
# PREPARE DATA FOR KUBERNETES ACCESS
# ----------------------------------------------------------------------------------------------------------------------


provider "helm" {
  kubernetes {
    token                  =
    host                   =
    cluster_ca_certificate =
  }
}

# ----------------------------------------------------------------------------------------------------------------------
# PREPARE KUBERNETES ACCESS
# ----------------------------------------------------------------------------------------------------------------------

provider "kubernetes" {
  host                   =
  token                  =
  cluster_ca_certificate =
}