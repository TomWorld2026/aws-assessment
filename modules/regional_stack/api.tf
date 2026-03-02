resource "aws_apigatewayv2_api" "api" {

  name          = "candidate-api-${var.region}"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "greet" {

  api_id = aws_apigatewayv2_api.api.id

  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.greeter.invoke_arn
}

resource "aws_apigatewayv2_route" "greet" {

  api_id    = aws_apigatewayv2_api.api.id
  route_key = "POST /greet"

  target = "integrations/${aws_apigatewayv2_integration.greet.id}"
}

output "api_url" {
  value = aws_apigatewayv2_api.api.api_endpoint
}