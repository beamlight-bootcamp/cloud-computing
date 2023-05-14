import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
 
    bucket_name = 'my-bucket'  # Replace with your desired bucket name
 
    response = s3_client.create_bucket(Bucket=bucket_name)
 
    return f"S3 bucket {bucket_name} created successfully."
