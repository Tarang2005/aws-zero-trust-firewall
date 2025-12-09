import boto3
from botocore.exceptions import ClientError

def auto_remediate():
    ec2 = boto3.client('ec2')
    print("ENFORCER PROTOCOL INITIATED...")
    
    try:
        response = ec2.describe_security_groups()
        security_groups = response['SecurityGroups']
        
        for sg in security_groups:
            for permission in sg['IpPermissions']:
                
                if 'FromPort' in permission and permission['FromPort'] == 22:
                    for ip_range in permission['IpRanges']:
                        cidr = ip_range.get('CidrIp')
                        
                        if cidr == '0.0.0.0/0':
                            print(f"TARGET IDENTIFIED: {sg['GroupId']} has Port 22 Open.")
                            
                            print(f"REVOKING ACCESS for {sg['GroupId']}...")
                            
                            ec2.revoke_security_group_ingress(
                                GroupId=sg['GroupId'],
                                IpProtocol='tcp',
                                FromPort=22,
                                ToPort=22,
                                CidrIp='0.0.0.0/0'
                            )
                            
                            print(f"THREAT NEUTRALIZED. Rule deleted.")
                            print("----------------------------------------")

    except ClientError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    auto_remediate()