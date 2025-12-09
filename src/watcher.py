import boto3
from botocore.exceptions import ClientError

def scan_security_groups():
    print("Connecting to AWS Mumbai Region...")
    ec2 = boto3.client('ec2')
    print("Scanning for dangerours open ports...")
    try:
        response = ec2.describe_security_groups()
        security_groups = response['SecurityGroups']
        
        risk_count = 0
        
        for sg in security_groups:
            for permission in sg['IpPermissions']:
                if 'FromPort' in permission and permission ['FromPort'] == 22:
                    for ip_range in permission['IpRanges']:
                        cidr = ip_range.get('CidrIp')
                
                        if cidr == '0.0.0.0/0':
                            print(f"Risk found in Group '{sg['GroupName']}' ({sg['GroupId']})")
                            print(f"   └── Port 22 is OPEN to the world! Hackers love this.")
                            risk_count += 1
                if risk_count == 0:
                    print("All systems safe. No open SSH ports found.")
                else:
                    print(f"Found {risk_count} security risks.")

    except ClientError as e:
        print(f"Error: Could not connect to AWS. Check your keys! \n{e}")
if __name__ == '__main__':
    scan_security_groups()        