variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "sre-challenge-flaschenpost"
}

variable "location" {
  description = "The location for resources"
  type        = string
  default     = "westeurope"
}

variable "storage_account_name" {
  description = "Name of the storage account"
  type        = string
  default     = "srechalngforflaschenpost"    # name was too long, and also name must be uniqu
}

variable "container_name" {
  description = "Name of the storage container"
  type        = string
  default     = "sre"
}
