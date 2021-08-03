  
import boto3
import json
import configparser
from config_update import config_updatee
from create_iamRole import create_iam_role
from botocore.exceptions import ClientError


## Read in Configuration Params

config = configparser.ConfigParser()
config.read_file(open('func.cfg'))

KEY                    = config.get('AWS','KEY')
SECRET                 = config.get('AWS','SECRET')

## Creating Redshift, S3 and IAM, EC2 clients

iam = boto3.client("iam",
                    region_name="us-west-2",
                    aws_access_key_id=KEY,
                    aws_secret_access_key=SECRET
                    )

redshift = boto3.client("redshift",
                    region_name="us-west-2",
                    aws_access_key_id=KEY,
                    aws_secret_access_key=SECRET
                    )

s3 = boto3.resource("s3",
                    region_name="us-west-2",
                    aws_access_key_id=config.get('AWS','KEY'),
                    aws_secret_access_key=config.get('AWS','SECRET')
                    )

ec2 = boto3.resource("ec2",
                    region_name="us-west-2",
                    aws_access_key_id=KEY,
                    aws_secret_access_key=SECRET
                    )




create_iam_role(config, iam)