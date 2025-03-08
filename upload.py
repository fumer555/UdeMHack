import boto3
import os
from set_env import set_env
# s3 = boto3.client('s3')
# s3.upload_file('audio.wav', 'fumer555-bucket-1', 'audio.wav')

set_env()
aws_access_key = os.environ.get("AWS_ACCESS_KEY")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key, region_name='us-east-2')

# Upload the file
bucket_name = 'fumer555-bucket-1'
file_path = 'yin.png'
s3_key = 'images/yin_1.png'

s3.upload_file(file_path, bucket_name, s3_key)
print(f"File uploaded to s3://{bucket_name}/{s3_key}")