resource "aws_vpc" "exercise-vpc" {
  cidr_block       = "10.0.0.0/16"

  tags = {
    Name = "exercise-vpc"
  }
}

output "vpc-id" {
  value = aws_vpc.exercise-vpc.id
}