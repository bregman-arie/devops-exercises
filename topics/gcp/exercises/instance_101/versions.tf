terraform {
    required_version = ">=1.3.0"

    required_providers {
        google = {
            source  = "hashicorp/google"
            version = ">= 4.10.0, < 5.0"
        }
    }
}