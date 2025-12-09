import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    print("ZeroTrust Function Started...")
    
    remediated_count = 0
    
    try:
        response = ec2.describe_security_groups()
        
        for sg in response['SecurityGroups']:
            for permission in sg['IpPermissions']:
                if 'FromPort' in permission and permission['FromPort'] == 22:
                    for ip_range in permission['IpRanges']:
                        if ip_range.get('CidrIp') == '0.0.0.0/0':
                            
                            print(f"ALERT: Found Open Port 22 in {sg['GroupId']}")
                            
                            ec2.revoke_security_group_ingress(
                                GroupId=sg['GroupId'],
                                IpProtocol='tcp',
                                FromPort=22,
                                ToPort=22,
                                CidrIp='0.0.0.0/0'
                            )
                            print(f"REVOVED access for {sg['GroupId']}")
                            remediated_count += 1
                            
        return {
            'statusCode': 200,
            'body': json.dumps(f'Scan Complete. Fixed {remediated_count} risks.')
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error executing remediation')
        }
