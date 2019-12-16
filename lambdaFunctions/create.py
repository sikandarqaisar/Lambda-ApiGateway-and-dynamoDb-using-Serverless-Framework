import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = (event['body'])
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'id': str(uuid.uuid1()),
        'text': data,
        'checked': False
    }
    # write the todo to the database
    table.put_item(Item=item)
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response