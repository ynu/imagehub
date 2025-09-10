import boto3
import os
import sys
from botocore.config import Config

def upload_file(file_path, file_name):
    # Get environment variables
    endpoint = os.environ['RUSTFS_ENDPOINT']
    access_key = os.environ['RUSTFS_ACCESS_KEY']
    secret_key = os.environ['RUSTFS_SECRET_KEY']
    bucket = os.environ['RUSTFS_BUCKET']

    # Configure the S3 client
    s3_client = boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(
            signature_version='s3v4',
            region_name='cn-east-1'
        )
    )

    # Upload the file
    try:
        with open(file_path, 'rb') as f:
            s3_client.put_object(
                Bucket=bucket,
                Key=file_name,
                Body=f
            )
        print(f"Successfully uploaded {file_name}")
        return True
    except Exception as e:
        print(f"Failed to upload {file_name}: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python upload_file.py <file_path> <file_name>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_name = sys.argv[2]
    
    if upload_file(file_path, file_name):
        sys.exit(0)
    else:
        sys.exit(1)