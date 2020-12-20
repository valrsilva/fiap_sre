provider "aws" {
    version = "~> 2.17"
    region = "us-east-1"
}

module "localfile" {
  source = "./modules/file"
  filename = "your-file-name"
}

resource "aws_sqs_queue" "terraform_queue_deadletter" {
  name = "terraform-example-queue-deadletter_${terraform.workspace}"
  delay_seconds = 90
  max_message_size = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
}

resource "aws_sqs_queue" "terraform_queue" {
  name = "terraform-example-queue_${terraform.workspace}"
  delay_seconds = 90
  max_message_size = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  redrive_policy = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.terraform_queue_deadletter.arn}\",\"maxReceiveCount\":1}"
}

resource "aws_sns_topic" "terraform_updates" {
  name = "terraform-updates-topic_${terraform.workspace}"
}

resource "aws_sns_topic_subscription" "terraform_updates_sqs_target" {
    topic_arn = "${aws_sns_topic.terraform_updates.arn}"
    protocol  = "sqs"
    endpoint  = "${aws_sqs_queue.terraform_queue.arn}"
}