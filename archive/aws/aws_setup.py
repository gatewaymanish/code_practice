import boto3

# AWS_ACCESS_KEY = ''
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_REGION = 'ap-south-1'


def init_aws():
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    return session



