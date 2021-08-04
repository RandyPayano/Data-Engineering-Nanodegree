import time
def cluster_status_traffic(cluster_id, redshift_client):
    """Verifies status of AWS redshift cluster and assures is available before proceeding
    Args:
      redshift_client (Client): Redshift Client
      cluster_id (string): AWS Redshift Cluster Name
    Returns:
      str: AWS Redshift Cluster Information
    """
    while True:
        response = redshift_client.describe_clusters(ClusterIdentifier=cluster_id)
        cluster_info = response['Clusters'][0]
        cluster_status = cluster_info['ClusterStatus']
        print(f"Cluster status: {cluster_status}")
        if cluster_status  == 'available':
            break
        time.sleep(60)

    return cluster_status 