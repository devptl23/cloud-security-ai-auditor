provider "aws" {
  region = "us-east-1"
}

# This is the "Safe" bucket
resource "aws_s3_bucket" "secure_storage" {
  bucket = "dev-patel-secure-data-2026"
}

# This is the "Vulnerable" bucket for our AI to find
resource "aws_s3_bucket" "vulnerable_storage" {
  bucket = "dev-patel-vulnerable-data-2026"
}
