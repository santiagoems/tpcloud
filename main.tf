# DynamoDB tables
resource "aws_dynamodb_table" "tweets_raw" {
  name           = "tweets-raw"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  range_key      = "subject"  # Sort key
  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "subject"
    type = "S"
  }
}

resource "aws_dynamodb_table" "tweets_processed" {
  name           = "tweets-processed"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  range_key      = "subject"  # Sort key
  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "subject"
    type = "S"
  }
}

resource "aws_ecr_repository" "sentimental-analysis-ecr" {
  name = "sentimental-analysis-ecr"
  tags = {
    Name        = "sentimental-analysis-ecr"
  }
}

resource "aws_ecs_cluster" "compute_cluster"{
  name = "sentimental-analysis-cluster"
  tags = {
    Name        = "sentimental-analysis-cluster"
  }

}

resource "aws_ecs_task_definition" "process_raw_tweets" {
  family                   = "ProcessRawTweets"
  network_mode             = "awsvpc"
  execution_role_arn       = "arn:aws:iam::493048853935:role/LabRole"
  task_role_arn            = "arn:aws:iam::493048853935:role/LabRole"
  cpu                      = "4096"
  memory                   = "8192"
  container_definitions = jsonencode([
    {
      name      = "ComputeInstance"
      image     = "052963506097.dkr.ecr.us-east-1.amazonaws.com/sentimental-analysis:latest"
      cpu       = 4096
      memory    = 8192
      essential = true
    }
  ])

  requires_compatibilities = ["FARGATE"]

  tags = {}
}

module "vpc" {
  source = "./modules/vpc"
}

module "apigw" {
  source = "./modules/apigw"
}