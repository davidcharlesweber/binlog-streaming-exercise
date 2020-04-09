import os
import boto3
from datetime import datetime, date
from requests_aws4auth import AWS4Auth

region = os.environ['AWS_DEFAULT_REGION']
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, 'es', session_token=credentials.token)

def serialize(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()
    else:
        return str(o)

def get_secret():
    secret_name = os.environ['SECRET']
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        raise e
    else:
        return get_secret_value_response['SecretString']
