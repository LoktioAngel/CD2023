import boto3
session = boto3.Session()
s3Client = session.client('s3')
x = s3Client.list_buckets()
for item in x['Buckets']:
    print(item['Name'])
