######################################
#
#   Author: Duc Dong
#   Get data from DynamoDB Table
#

import json
import boto3
from boto3.dynamodb.conditions import Key

def getViewCount(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
    viewCountTable = dynamodb.Table('views_db')

    numOfViews = viewCountTable.get_item(Key={'NumViews': 'current'})['Item']['currentNumViews']
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "numberOfViews": str(numOfViews),
        }),
    }