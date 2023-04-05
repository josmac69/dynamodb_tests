import boto3
import configparser

def get_dynamodb_table_names():
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

    # Get a list of all table names
    print('\nGetting a list of all table names')
    table_names = []
    response = dynamodb.list_tables()
    table_names = response['TableNames']

    # Return the table names
    return table_names

if __name__ == '__main__':
    # Call the get_dynamodb_table_names function
    print('Calling the get_dynamodb_table_names function')
    table_names = get_dynamodb_table_names()

    # Print the table names
    print('\nPrinting the table names')
    for name in table_names:
        print(name)