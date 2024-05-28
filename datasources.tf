data "archive_file" "consult_db_lambda" {
  type        = "zip"
  source_file  = "./lambdas/consult_db.py"
  output_path = "./lambdas/consult_db.zip"
}

data "archive_file" "tweets_raw_lambda" {
  type        = "zip"
  source_file  = "./lambdas/tweets_raw.py"
  output_path = "./lambdas/tweets_raw.zip"
}


data "archive_file" "add_tweet_lambda" {
  type        = "zip"
  source_file  = "./lambdas/add_tweet.py"
  output_path = "./lambdas/add_tweet.zip"
}

data "archive_file" "update_db_lambda" {
  type        = "zip"
  source_file  = "./lambdas/update_db.py"
  output_path = "./lambdas/update_db.zip"
}