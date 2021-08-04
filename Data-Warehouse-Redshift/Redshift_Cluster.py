import pandas as pd
import boto3
import json
import psycopg2
import configparser

def create_redshift_cluster(cfg_file_path, redshift_client):
    """Creates AWS redshift cluster

    Args:
        cfg_file_path (string): Path to configuration file
        redshift_client ([type]): [description]

    Returns:
        [type]: [description]
    """

    config = configparser.ConfigParser()
    config.read_file(open(cfg_file_path))

    KEY                    = config.get('AWS','KEY')
    SECRET                 = config.get('AWS','SECRET')
    roleArn                = config.get('AWS','rolearn')
    DWH_CLUSTER_TYPE       = config.get("DWH","DWH_CLUSTER_TYPE")
    DWH_NUM_NODES          = config.get("DWH","DWH_NUM_NODES")
    DWH_NODE_TYPE          = config.get("DWH","DWH_NODE_TYPE")
    DWH_CLUSTER_IDENTIFIER = config.get("DWH","DWH_CLUSTER_IDENTIFIER")
    DWH_DB                 = config.get("DWH","DWH_DB")
    DWH_DB_USER            = config.get("DWH","DWH_DB_USER")
    DWH_DB_PASSWORD        = config.get("DWH","DWH_DB_PASSWORD")
    DWH_PORT               = config.get("DWH","DWH_PORT")
    DWH_IAM_ROLE_NAME      = config.get("DWH", "DWH_IAM_ROLE_NAME")

    # Check if cluster already exists
    try:
        response = redshift_client.describe_clusters(ClusterIdentifier=config.get('CLUSTER', 'CLUSTERIDENTIFIER'))
        print('Cluster already exists: ' + response['Clusters'][0]['ClusterIdentifier'])
        return None
    except:
        response = None

    # If not create Cluster
    if response is None:
        try:
            print("-"*15, "Creating Cluster")
            response = redshift_client.create_cluster(        
                # hardware
                ClusterType=DWH_CLUSTER_TYPE,
                NodeType=DWH_NODE_TYPE,
                NumberOfNodes=int(DWH_NUM_NODES),   
                
                # identifiers & credentials
                    DBName=DWH_DB,
                    ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,
                    MasterUsername=DWH_DB_USER,
                    MasterUserPassword=DWH_DB_PASSWORD,
                
                # parameter for role (to allow s3 access)
                IamRoles=[roleArn]
            
            )
            print("Redshift Cluster created")
            return response['Cluster']

        except Exception as e:
            print(f"Error {e}")
            return None