# aws create a vpc with one subnet

from archive.aws.aws_setup import init_aws


session = init_aws()

ec2 = session.client('ec2')


def create_vpc():
    # Create VPC
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']
    print(f'VPC Created: {vpc_id}')

    # Tag the VPC
    ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": "MyVPC"}])


    # Create Subnet
    subnet_response = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
    subnet_id = subnet_response['Subnet']['SubnetId']
    print(f'Subnet Created: {subnet_id}')


# Describe VPCs
vpcs = ec2.describe_vpcs()
print(vpcs)
# output: {'Vpcs': [{'OwnerId': '552683392283', 'InstanceTenancy': 'default', 'CidrBlockAssociationSet': [{'AssociationId': 'vpc-cidr-assoc-02efeeaa4f5bc982a', 'CidrBlock': '172.31.0.0/16', 'CidrBlockState': {'State': 'associated'}}], 'IsDefault': True, 'BlockPublicAccessStates': {'InternetGatewayBlockMode': 'off'}, 'VpcId': 'vpc-04bdc99c406da012a', 'State': 'available', 'CidrBlock': '172.31.0.0/16', 'DhcpOptionsId': 'dopt-04cddc40132659689'}, {'OwnerId': '552683392283', 'InstanceTenancy': 'default', 'CidrBlockAssociationSet': [{'AssociationId': 'vpc-cidr-assoc-013a13c3d57423558', 'CidrBlock': '10.0.0.0/16', 'CidrBlockState': {'State': 'associated'}}], 'IsDefault': False, 'Tags': [{'Key': 'Name', 'Value': 'MyVPC'}], 'BlockPublicAccessStates': {'InternetGatewayBlockMode': 'off'}, 'VpcId': 'vpc-015461938ea2b2aa6', 'State': 'available', 'CidrBlock': '10.0.0.0/16', 'DhcpOptionsId': 'dopt-04cddc40132659689'}], 'ResponseMetadata': {'RequestId': '377ed0c5-ec38-4411-a227-98ce383f5155', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '377ed0c5-ec38-4411-a227-98ce383f5155', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1451', 'date': 'Tue, 20 May 2025 19:27:02 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

# Describe Subnets
subnets = ec2.describe_subnets()
print(subnets)
# output: {'Subnets': [{'AvailabilityZoneId': 'aps1-az2', 'MapCustomerOwnedIpOnLaunch': False, 'OwnerId': '552683392283', 'AssignIpv6AddressOnCreation': False, 'Ipv6CidrBlockAssociationSet': [], 'SubnetArn': 'arn:aws:ec2:ap-south-1:552683392283:subnet/subnet-09e5cccc443b46891', 'EnableDns64': False, 'Ipv6Native': False, 'PrivateDnsNameOptionsOnLaunch': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'BlockPublicAccessStates': {'InternetGatewayBlockMode': 'off'}, 'SubnetId': 'subnet-09e5cccc443b46891', 'State': 'available', 'VpcId': 'vpc-04bdc99c406da012a', 'CidrBlock': '172.31.16.0/20', 'AvailableIpAddressCount': 4091, 'AvailabilityZone': 'ap-south-1c', 'DefaultForAz': True, 'MapPublicIpOnLaunch': True}, {'AvailabilityZoneId': 'aps1-az3', 'MapCustomerOwnedIpOnLaunch': False, 'OwnerId': '552683392283', 'AssignIpv6AddressOnCreation': False, 'Ipv6CidrBlockAssociationSet': [], 'SubnetArn': 'arn:aws:ec2:ap-south-1:552683392283:subnet/subnet-0a165d7c13883101e', 'EnableDns64': False, 'Ipv6Native': False, 'PrivateDnsNameOptionsOnLaunch': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'BlockPublicAccessStates': {'InternetGatewayBlockMode': 'off'}, 'SubnetId': 'subnet-0a165d7c13883101e', 'State': 'available', 'VpcId': 'vpc-015461938ea2b2aa6', 'CidrBlock': '10.0.1.0/24', 'AvailableIpAddressCount': 251, 'AvailabilityZone': 'ap-south-1b', 'DefaultForAz': False, 'MapPublicIpOnLaunch': False}, {'AvailabilityZoneId': 'aps1-az1', 'MapCustomerOwnedIpOnLaunch': False, 'OwnerId': '552683392283', 'AssignIpv6AddressOnCreation': False, 'Ipv6CidrBlockAssociationSet': [], 'SubnetArn': 'arn:aws:ec2:ap-south-1:552683392283:subnet/subnet-0e744f0fcb1a309e0', 'EnableDns64': False, 'Ipv6Native': False, 'PrivateDnsNameOptionsOnLaunch': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'BlockPublicAccessStates': {'InternetGatewayBlockMode': 'off'}, 'SubnetId': 'subnet-0e744f0fcb1a309e0', 'State': 'available', 'VpcId': 'vpc-04bdc99c406da012a', 'CidrBlock': '172.31.32.0/20', 'AvailableIpAddressCount': 4091, 'AvailabilityZone': 'ap-south-1a', 'DefaultForAz': True, 'MapPublicIpOnLaunch': True}, {'AvailabilityZoneId': 'aps1-az3', 'MapCustomerOwnedIpOnLaunch': False, 'OwnerId': '552683392283', 'AssignIpv6AddressOnCreation': False, 'Ipv6CidrBlockAssociationSet': [], 'SubnetArn': 'arn:aws:ec2:ap-south-1:552683392283:subnet/subnet-0f76be105b74ca4cd', 'EnableDns64': False, 'Ipv6Native': False, 'PrivateDnsNameOptionsOnLaunch': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'BlockPublicAccessStates': {'InternetGatewayBlockMode': 'off'}, 'SubnetId': 'subnet-0f76be105b74ca4cd', 'State': 'available', 'VpcId': 'vpc-04bdc99c406da012a', 'CidrBlock': '172.31.0.0/20', 'AvailableIpAddressCount': 4091, 'AvailabilityZone': 'ap-south-1b', 'DefaultForAz': True, 'MapPublicIpOnLaunch': True}], 'ResponseMetadata': {'RequestId': 'eed8e86c-7eb0-47bc-89e8-7e253fb42afe', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'eed8e86c-7eb0-47bc-89e8-7e253fb42afe', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '4498', 'date': 'Tue, 20 May 2025 19:27:02 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}