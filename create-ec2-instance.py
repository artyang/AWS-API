import boto3

# AWS credentials
access_key = 'YOUR_ACCESS_KEY'
secret_key = 'YOUR_SECRET_KEY'
region = 'us-west-1'  # Replace with your desired region

# S3 bucket configuration
bucket_name = 'your-bucket-name'  # Replace with your desired bucket name

# Create an S3 client
s3_client = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Create an S3 bucket
response = s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': region}
)

# Check the response
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print(f"Successfully created S3 bucket: {bucket_name}")
else:
    print("Failed to create S3 bucket")
    print(response)
