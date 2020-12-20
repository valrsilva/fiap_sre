import boto3
import json

def lambda_handler(event, context):
    data = json.dumps(event)
    
    print(data)

    return {
        'statusCode': 200,
        'body': json.dumps(data)
 }