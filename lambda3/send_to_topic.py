import json
import boto3

def lambda_handler(event, context):
    
    message = json.dumps(event)
    sns = boto3.client('sns')
    sns.publish(TopicArn='arn:aws:sns:us-east-1:331437564581:terraform-updates-topic_dev',Message=message)
    
    print(message)

    return {
      'statusCode': 200,
      'body': json.dumps(message)
    }