from __future__ import print_function
import boto3
import os

region = os.environ.get('AWS_DEFAULT_REGION')

dynamodb = boto3.resource('dynamodb', region_name=region)

tabla_Services = dynamodb.create_table(
    TableName='Services',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH' #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)