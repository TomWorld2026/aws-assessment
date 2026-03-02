module "cognito" {
  source = "./modules/cognito"

  email = var.email
}

module "stack_us" {

  source = "./modules/regional_stack"

  region           = "us-east-1"
  cognito_pool_arn = module.cognito.pool_arn
  email            = var.email
  repo_url         = var.repo_url
  sns_topic        = var.sns_topic

  providers = {
    aws = aws
  }
}

module "stack_eu" {

  source = "./modules/regional_stack"

  region           = "eu-west-1"
  cognito_pool_arn = module.cognito.pool_arn
  email            = var.email
  repo_url         = var.repo_url
  sns_topic        = var.sns_topic

  providers = {
    aws = aws.eu
  }
}