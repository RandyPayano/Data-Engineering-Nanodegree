def create_cluster_security_group():
  """Creates VPC Security Group on AWS
  Returns:
      string: Security Group ID
  """
  try:
    response = ec2_client.describe_security_groups(Filters= [{"Name": "group-name", "Values": [config.get('SECURITY', 'SG_Name')]}])
  except ClientError as e:
     print(e)

  if len(response['SecurityGroups']) > 0:
    print('Security Group already exists: ' + response['SecurityGroups'][0]['GroupId'])
    return response['SecurityGroups'][0]['GroupId']
  else:
    response = None

  if response is None:
    vpc_id = config.get('SECURITY', 'VPC_ID')
    if vpc_id == "":
      response = ec2_client.describe_vpcs()
      vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

    try:
        response = ec2_client.create_security_group(GroupName=config.get('SECURITY', 'SG_Name'),Description='Redshift security group',VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

        ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 5439,
                 'ToPort': 5439,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ])
        return security_group_id
    except ClientError as e:
        print(e)