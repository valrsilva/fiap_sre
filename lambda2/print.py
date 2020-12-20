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

def lambda_handler(event, context):
    data = json.dumps(event)
    
    print(data)

    return {
        'statusCode': 200,
        'body': json.dumps(data)
 }