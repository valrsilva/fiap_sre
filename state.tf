terraform {
  backend "s3" {
    bucket = "lab-fiap-336947"
    key    = "trabalho"
    region = "us-east-1"
  }
}