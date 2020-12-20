resource "aws_s3_bucket" "b" {
  bucket = "lab-fiap-336947"
  acl    = "private"

  tags = {
    Name        = "lab-fiap-336947"
    Environment = "admin"
  }
}