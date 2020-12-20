import sys
sys.path.insert(0, '/opt')

import boto3
import json

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

xray_recorder.configure(service='trabalho10')
plugins = ('ElasticBeanstalkPlugin', 'EC2Plugin')
xray_recorder.configure(plugins=plugins)
patch_all()


from sqsHandler import SqsHandler
from random import randrange

message = ""

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    message = body['message']

    print(message)

    dest = findDest(message)
    print(dest)

    return{
       'statusCode': 200,
       'body':json.dumps(message)
    }

def findDest(message):
    
    num = randrange(10)
    
    # Tentamos induzir uma mensagem ao erro para que esta seja redirecionada à SQS DLQ
    if num >= 5:
        print (num)
        sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/331437564581/terraform-example-queue_dev')
        sqs.send(message)
        send = "Message send to Principal"
        
    else:
        print (num)
        sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/331437564581/terraform-example-queue-deadletter_dev')
        sqs.send(message)
        send = "Message send to DLQ"
    
    return {
        send
    }