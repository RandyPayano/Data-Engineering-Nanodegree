  
import boto3
import json
import configparser
from config_update import config_update
from Iam_Role import create_iam_role, delete_iam_role
from Redshift_Cluster import create_redshift_cluster
from botocore.exceptions import ClientError


## Read in Configuration Params

config_path = 'func.cfg'

config = configparser.ConfigParser()
config.read_file(open(config_path))

KEY                    = config.get('AWS','KEY')
SECRET                 = config.get('AWS','SECRET')

## Creating Redshift, S3 and IAM, EC2 clients

iam_client = boto3.client("iam",
                    region_name="us-west-2",
                    aws_access_key_id=KEY,
                    aws_secret_access_key=SECRET
                    )

redshift_client = boto3.client("redshift",
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



#create_iam_role(config_path, iam_client)

#delete_iam_role(config_path, iam_client)

create_redshift_cluster(config_path, redshift_client)