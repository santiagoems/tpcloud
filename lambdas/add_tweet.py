import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table_name = 'tweets-raw'


def lambda_handler(event, context):
    try:

        tweet_id = str(uuid.uuid4())
        event_body = json.loads(event['body'])

        subject = event_body['subject']
        user = event_body['user']
        text = event_body['text']

        if not (user and text and subject):
            return {
                "statusCode": 400,
                "body": json.dumps(event)
            }

        table = dynamodb.Table(table_name)

        table.put_item(
            Item={
                'id': tweet_id,
                'subject': subject,
                'user': user,
                'text': text
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Tweet added successfully", "tweet_id": tweet_id})
        }
    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing key: {str(e)} in request body"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }