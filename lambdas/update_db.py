import json
import boto3

dynamodb = boto3.resource('dynamodb')
source_table_name = 'tweets-raw'
destination_table_name = 'tweets-processed'


def lambda_handler(event, context):
    try:
        # Access the source table
        source_table = dynamodb.Table(source_table_name)

        # Load tweets from the body of the event
        tweets = json.loads(event['body'])

        # Delete each item from the source table
        for tweet in tweets:
            # Construct the key including both the partition key ('id') and the sort key ('subject')
            key = {'id': tweet['id'], 'subject': tweet['subject']}
            source_table.delete_item(Key=key)

        # Access the destination table
        destination_table = dynamodb.Table(destination_table_name)

        # Add each tweet to the destination table
        for tweet in tweets:
            destination_table.put_item(Item=tweet)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Tweets added to the destination table"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
