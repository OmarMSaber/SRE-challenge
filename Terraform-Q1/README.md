### Introduction

This Terraform project provisions \[Azure resource Group, Azure Storage account, Azure Storage account container\].

### Prerequisites

*   Terraform (v1+)
    
*   Azure CLI 
    
*   Azure subscription ID
    

### Getting Started

#### Set Up Environment

Ensure Terraform and Azure CLI are installed and configured.

#### Configure Variables

Create a terraform.tfvars file and add your subscription ID 

Terraform

`   subscription_id = "your-subscription-id"   `


### Usage

#### Initialize Terraform


`   terraform init   `


#### Plan the Changes


`   terraform plan -out=tfplan   `


#### Review the Plan

Carefully examine the output to ensure it matches your desired infrastructure.

#### Apply the Changes

`   terraform apply tfplan   `


### Additional Commands

#### Destroy Infrastructure

`   terraform destroy   `

**Note:** The `terraform.tfstate.output` file is now obsolete, as the resources have been destroyed and the contents are no longer functional.


#### Other Commands

*  ` terraform output `- To view output values.
    
*  ` terraform state list `- To list resources.
