import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table_name = 'tweets-processed'

def lambda_handler(event, context):
    try:
        # Charger le corps JSON en un dictionnaire Python
        body = json.loads(event['body'])

        # Accéder à la clé 'word' dans le corps JSON
        word = body['word']

        if not word:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "The 'word' parameter is required"})
            }

        # Accéder à la table DynamoDB
        table = dynamodb.Table(table_name)

        # Effectuer un scan avec une condition de filtre basée sur 'word'
        response = table.scan(
            FilterExpression=Attr('text').contains(word)
        )

        # Obtenir les éléments de la réponse
        items = response.get('Items', [])

        # Retourner les éléments au format JSON
        return {
            "statusCode": 200,
            "body": json.dumps({"results": items})
        }
    except KeyError as e:
        # Gérer KeyError si la clé 'word' est manquante
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'word' key in request body"})
        }
    except Exception as e:
        # Retourner un message d'erreur si quelque chose ne va pas
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }