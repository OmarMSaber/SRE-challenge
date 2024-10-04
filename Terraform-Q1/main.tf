# Azure Resource Group
resource "azurerm_resource_group" "sre_challenge" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    department = "SRE"
  }
}

# Storage Account
resource "azurerm_storage_account" "sre_challenge" {
  name                     = var.storage_account_name
  resource_group_name       = azurerm_resource_group.sre_challenge.name
  location                  = azurerm_resource_group.sre_challenge.location
  account_tier              = "Standard"
  account_replication_type  = "LRS"
  access_tier               = "Hot"

  tags = {
    department = "SRE"
  }
}

# Storage Account Container
resource "azurerm_storage_container" "sre_container" {
  name                  = var.container_name
  storage_account_name   = azurerm_storage_account.sre_challenge.name
  container_access_type  = "private"
}
