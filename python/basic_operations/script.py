"""Basic operations with DynamoDB"""
import boto3
import configparser

def main():
    """Main function"""
        # Read login credentials from a configuration file
    print('\nReading credentials from /secrets/dynamodb_credentials.ini')
    config = configparser.ConfigParser()
    config.read('/secrets/dynamodb_credentials.ini')
    print('Access Key ID: ' + config['DEFAULT']['AWS_ACCESS_KEY_ID'])
    print('Secret Access Key: ' + config['DEFAULT']['AWS_SECRET_ACCESS_KEY'])
    print('Region: ' + config['DEFAULT']['REGION'])
    print('Endpoint URL: ' + config['DEFAULT']['ENDPOINT_URL'])

    # Create a DynamoDB client
    print('\nCreating a DynamoDB client')
    dynamodb = boto3.client(
        'dynamodb'
        ,aws_access_key_id=config['DEFAULT']['AWS_ACCESS_KEY_ID']
        ,aws_secret_access_key=config['DEFAULT']['AWS_SECRET_ACCESS_KEY']
        ,region_name=config['DEFAULT']['REGION']
        ,endpoint_url=config['DEFAULT']['ENDPOINT_URL']
    )

    # create a new table
    print('\nCreating a new table')
    table_name = 'example_table'
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    # wait for the table to be created
    print('\nWaiting for the table to be created')
    dynamodb.get_waiter('table_exists').wait(TableName=table_name)

    # modify the table schema
    print('\nModifying the table schema')
    dynamodb.update_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            }
        ],
        GlobalSecondaryIndexUpdates=[
            {
                'Create': {
                    'IndexName': 'name_index',
                    'KeySchema': [
                        {
                            'AttributeName': 'name',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'id',
                            'KeyType': 'RANGE'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                    }
                }
            }
        ]
    )

    # insert some data
    print('\nInserting some data')
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'id': {'N': '1'},
            'name': {'S': 'Alice'},
            'age': {'N': '30'}
        }
    )

    # update some data
    print('\nUpdating some data')
    dynamodb.update_item(
        TableName=table_name,
        Key={
            'id': {'N': '1'}
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': {'N': '35'}
        }
    )

    # get some data
    print('\nGetting some data')
    response = dynamodb.get_item(
        TableName=table_name,
        Key={
            'id': {'N': '1'}
        }
    )
    item = response['Item']
    print(item)

if __name__ == '__main__':
    main()
