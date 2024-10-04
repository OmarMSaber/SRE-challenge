# Specify Terraform version and provider versions
terraform {
  required_version = ">= 1.0.0"  # Ensures Terraform v1+ is used

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.0.0"       # Specifies minimum provider version
    }
  }
}

# Azure Provider Configuration
provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}
