#########################################################
#
#   Author: Duc Dong
#   Increase current number of views by 1 in DynamoDB
#

import json
import boto3
from boto3.dynamodb.conditions import Key

def updateViewCount(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
    viewCountTable = dynamodb.Table('views_db')

    # Get entry from DynamoDB
    viewCountTableEntry = viewCountTable.get_item(Key={'NumViews': "current"})["Item"]
    # Increase counter
    viewCountTableEntry["currentNumViews"] += 1
    # Update entry in DynamoDB
    viewCountTable.put_item(Item=viewCountTableEntry)

    return {
        "statusCode": 200
    }