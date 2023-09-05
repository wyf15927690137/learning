import boto3

access_key = 'AKIAXC524U35PBOM7SG6'
secret_key = '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'


ec2 = boto3.client(
    service_name='ec2',
    region_name='us-east-1',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

instances = ec2.run_instances(
    ImageId='ami-0de00c4203899e9af',  # Replace with your desired Amazon Machine Image (AMI) ID
    InstanceType= 't2.micro',  # Replace with your desired instance type
    KeyName= 'yanfei_key',  # Replace with your desired key pair name
    MinCount= 1,
    MaxCount= 1
)

# Need EC2 Access in IAM Permissions
# The region name must be correctly set
# response = ec2.describe_instances()
# print(response)
# instances = response['Reservations'][0]['Instances']
# id = instances[0]['InstanceId']
# for instance in instances:
#     print(instance['InstanceId'], instance['State']['Name'])
#
# response = ec2.stop_instances(InstanceIds=[id])
# print(response)

# response = ec2.start_instances(InstanceIds=[id])
# print(response)

# response = ec2.terminate_instances(InstanceIds=[id])
# print(response)
response = ec2.describe_key_pairs()
print(response)

# response = ec2.create_key_pair(KeyName='MY_KEY_PAIR')
# print(response)
#
# response = ec2.delete_key_pair(KeyName='MY_KEY_PAIR')
# print(response)