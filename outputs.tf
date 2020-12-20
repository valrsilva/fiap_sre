output "filename" {
  value = "${module.localfile.filename}"
}

output "content" {
  value = "${module.localfile.content}"
}

output "terraform_queue_deadletterARN" {
  value = "${aws_sqs_queue.terraform_queue_deadletter.arn}"
}
output "terraform_queue_deadletterURL" {
  value = "${aws_sqs_queue.terraform_queue_deadletter.id}"
}
output "terraform_queueARN" {
  value = "${aws_sqs_queue.terraform_queue.arn}"
}
output "terraform_queueURL" {
  value = "${aws_sqs_queue.terraform_queue.id}"
}
output "terraform_updatesARN" {
  value = "${aws_sns_topic.terraform_updates.arn}"
}
