## create a vm through aws api call using python code

from archive.aws.aws_setup import init_aws

AMI_ID = 'ami-0af9569868786b23a'
KEY_NAME = 'demo1_keypair'
SUBNET_ID = 'subnet-0e744f0fcb1a309e0'
SECURITY_GROUP_ID = 'sg-05677e3ebbc7426fd'

session = init_aws()
ec2 = session.client('ec2')

response = ec2.run_instances(
    ImageId=AMI_ID,
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName=KEY_NAME,
    SubnetId=SUBNET_ID,
    SecurityGroupIds=[SECURITY_GROUP_ID],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyEC2Instance'}
            ]
        }
    ]
)

instance_id = response['Instances'][0]['InstanceId']
print(f'EC2 Instance Launched: {instance_id}')

## verify the instance
instances = ec2.describe_instances(InstanceIds=[instance_id])
print(instances)

# output:
# EC2 Instance Launched: i-0a331785279862806
# {'Reservations': [{'ReservationId': 'r-0b680ae2f306442c0', 'OwnerId': '552683392283', 'Groups': [], 'Instances': [{'Architecture': 'x86_64', 'BlockDeviceMappings': [], 'ClientToken': '344f0910-f7aa-40ad-9ec6-dc97431d136d', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2025, 5, 21, 9, 20, 59, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-0ee4adab64abaaa46', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attaching', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupId': 'sg-05677e3ebbc7426fd', 'GroupName': 'default'}], 'Ipv6Addresses': [], 'MacAddress': '02:7a:80:1f:4f:31', 'NetworkInterfaceId': 'eni-041594f68234df5b4', 'OwnerId': '552683392283', 'PrivateDnsName': 'ip-172-31-39-159.ap-south-1.compute.internal', 'PrivateIpAddress': '172.31.39.159', 'PrivateIpAddresses': [{'Primary': True, 'PrivateDnsName': 'ip-172-31-39-159.ap-south-1.compute.internal', 'PrivateIpAddress': '172.31.39.159'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-0e744f0fcb1a309e0', 'VpcId': 'vpc-04bdc99c406da012a', 'InterfaceType': 'interface', 'Operator': {'Managed': False}}], 'RootDeviceName': '/dev/xvda', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupId': 'sg-05677e3ebbc7426fd', 'GroupName': 'default'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'MyEC2Instance'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'pending', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled', 'InstanceMetadataTags': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2025, 5, 21, 9, 20, 59, tzinfo=tzutc()), 'PrivateDnsNameOptions': {'HostnameType': 'ip-name', 'EnableResourceNameDnsARecord': False, 'EnableResourceNameDnsAAAARecord': False}, 'MaintenanceOptions': {'AutoRecovery': 'default'}, 'CurrentInstanceBootMode': 'legacy-bios', 'NetworkPerformanceOptions': {'BandwidthWeighting': 'default'}, 'Operator': {'Managed': False}, 'InstanceId': 'i-0a331785279862806', 'ImageId': 'ami-0af9569868786b23a', 'State': {'Code': 0, 'Name': 'pending'}, 'PrivateDnsName': 'ip-172-31-39-159.ap-south-1.compute.internal', 'PublicDnsName': '', 'StateTransitionReason': '', 'KeyName': 'demo1_keypair', 'AmiLaunchIndex': 0, 'ProductCodes': [], 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2025, 5, 21, 9, 20, 59, tzinfo=tzutc()), 'Placement': {'GroupName': '', 'Tenancy': 'default', 'AvailabilityZone': 'ap-south-1a'}, 'Monitoring': {'State': 'disabled'}, 'SubnetId': 'subnet-0e744f0fcb1a309e0', 'VpcId': 'vpc-04bdc99c406da012a', 'PrivateIpAddress': '172.31.39.159'}]}], 'ResponseMetadata': {'RequestId': 'bd427476-8145-47a0-af14-f5f4c5e6ea4f', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'bd427476-8145-47a0-af14-f5f4c5e6ea4f', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '4168', 'date': 'Wed, 21 May 2025 09:21:00 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
