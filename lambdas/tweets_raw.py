import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = 'tweets-raw'

def lambda_handler(event, context):
    try:
        # Access the DynamoDB table
        table = dynamodb.Table(table_name)

        # Perform a scan to retrieve all tweets
        response = table.scan()

        # Get the items from the response
        items = response.get('Items', [])

        # Return the items in JSON format
        return {
            "statusCode": 200,
            "body": json.dumps( items)
        }
    except Exception as e:
        # Return an error message if something goes wrong
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }