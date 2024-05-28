output "api_gateway_id" {
  value = aws_api_gateway_rest_api.sentimental_api.id
}

output "consult_db_resource_id" {
  value = aws_api_gateway_resource.consult_db_resource.id
}

output "tweets_raw_resource_id" {
  value = aws_api_gateway_resource.tweets_raw_resource.id
}

output "add_tweet_resource_id" {
  value = aws_api_gateway_resource.add_tweet_resource.id
}

output "update_db_resource_id" {
  value = aws_api_gateway_resource.update_db_resource.id
}

output "api_gateway_url" {
  value = "https://${aws_api_gateway_rest_api.sentimental_api.id}.execute-api.us-east-1.amazonaws.com/${aws_api_gateway_deployment.sentimental_api_deployment.stage_name}"
}