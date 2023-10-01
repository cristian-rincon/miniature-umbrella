variable "project_id" {
    type = string
    description = "The project ID to deploy resources to"
    default = "devops-sandbox-350820"
}

variable "region" {
    type = string
    description = "The region to deploy resources to"
    default = "us-central1"
}

variable "zone" {
    type = string
    description = "The zone to deploy resources to"
    default = "us-central1-a"
}