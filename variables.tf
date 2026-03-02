variable "email" {
  type = string
}

variable "repo_url" {
  type = string
}

variable "sns_topic" {
  default = "arn:aws:sns:us-east-1:637226132888:Candidate-Verification-Topic"
}