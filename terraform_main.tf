provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-healthcare-migration"
  location = "westeurope"
}

resource "azurerm_storage_account" "datalake" {
  name                     = "healthcaredl"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true
}
