# Expose Storage Account ID
output "storage_account_id" {
  description = "The ID of the Storage Account"
  value       = azurerm_storage_account.sre_challenge.id
}

# Expose Storage Account Primary Access Key
output "primary_access_key" {
  description = "The Primary Access Key for the Storage Account"
  value       = azurerm_storage_account.sre_challenge.primary_access_key
  sensitive   = true
}

# Expose Storage Account Primary Connection String
output "primary_connection_string" {
  description = "The Primary Connection String for the Storage Account"
  value       = azurerm_storage_account.sre_challenge.primary_connection_string
  sensitive   = true
}

# Expose Storage Container ID
output "storage_container_id" {
  description = "The ID of the Storage Account Container"
  value       = azurerm_storage_container.sre_container.id
}
