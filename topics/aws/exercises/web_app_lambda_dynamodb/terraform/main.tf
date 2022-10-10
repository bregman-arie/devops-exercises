provider "aws" {
  region = "us-west-1"
}

resource "aws_dynamodb_table" "users" {
  name     = "users"
  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "login"
    type = "S"
  }

  global_secondary_index {
    hash_key = 
    
  }
}
