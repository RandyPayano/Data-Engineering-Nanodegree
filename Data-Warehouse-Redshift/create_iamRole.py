import boto3
import configparser
import json
from config_update import config_updatee
import pandas as pd
## Read in Configuration Params

config = configparser.ConfigParser()
config.read_file(open('func.cfg'))

KEY                    = config.get('AWS','KEY')
SECRET                 = config.get('AWS','SECRET')

iam = boto3.client("iam",
                    region_name="us-west-2",
                    aws_access_key_id=KEY,
                    aws_secret_access_key=SECRET
                    )



def create_iam_role(cfg_file, iam):
    """Creates AWS iam role
    Args:
      config (ConfigParser object): Cfig File to update Resource configuration
      iam (Iam cliet): AWS iam client 
    Returns:
      dictionary: IAM Role Information
    """

    RoleName = cfg_file.get('DWH', 'DWH_IAM_ROLE_NAME')
    Policy_to_attach = cfg_file.get('AWS','PolicyArn')

    # Checking role does not already exists
    try:
        response = iam.get_role(RoleName=RoleName)
        print('iam Role already exists: ' + response['Role']['Arn'])
        return response
    except:
        response = None

    # Creating role
    if response is None:
        try:
            dwhRole = iam.create_role(
            RoleName = RoleName,
            Description = 'Allows Redshift to call AWS services on your behalf',
            AssumeRolePolicyDocument=json.dumps(
                {'Statement': [{'Action': 'sts:AssumeRole',
               'Effect': 'Allow',
               'Principal': {'Service': 'redshift.amazonaws.com'}}],
               'Version': '2012-10-17'})
            )

            # Attaching Policy to Role (defined in configuration file)
            iam.attach_role_policy(
                RoleName = RoleName,
                PolicyArn = Policy_to_attach
            )
            print(f"Created: IAM Role: {RoleName}, Policy attached: {Policy_to_attach}")
            print(pd.DataFrame(dwhRole["Role"]))
            return dwhRole

        except Exception as e:
          print(f"Error: {e}")

