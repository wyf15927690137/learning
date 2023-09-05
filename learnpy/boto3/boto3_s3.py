import boto3

access_key = 'AKIAXC524U35PBOM7SG6'
secret_key = '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'

# use boto3 resources
# s3 = boto3.resource(
#     service_name='s3',
#     region_name='us-east-1',
#     aws_access_key_id=access_key,
#     aws_secret_access_key=secret_key
# )
# # Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)

bucket_name = 'pythontestbucket1214'

client = boto3.client(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key

)
# list buckets
for bucket in client.list_buckets()['Buckets']:
    print(bucket['Name'])

# Create a new bucket
response = client.create_bucket(
    Bucket=bucket_name,
    # LocationConstraint must be correctly set
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'}
)

print(response)

# delete bucket
# response = client.delete_bucket(
#     Bucket=bucket_name
# )

print(response)

# upload file
client.upload_file('D:\\Files\\get-pip.py', 'yanfeibucket', 'get-pip.py')

# upload binary
with open(r'D:\Files\Python3\Python-3.7.9\build\lib.linux-x86_64-3.7\_asyncio.cpython-37m-x86_64-linux-gnu.so', 'rb') as data:
    client.upload_fileobj(data, 'yanfeibucket', '_asyncio.cpython-37m-x86_64-linux-gnu.so')