
import boto3
def lambda_handler(event, context):
    # Create EC2 resource
    ec2_resource = boto3.resource('ec2')
    
    # Specify the parameters for the new EC2 instance
    instance_params = {
        'ImageId': 'ami-08333bccc35d71140',  # Replace with the desired AMI ID
        'InstanceType': 't2.micro',  # Replace with the desired instance type
        'KeyName': 'key101',   # Replace with your key pair name
        'MinCount': 1,
        'MaxCount': 1
    }
    
    # Launch the EC2 instance
    new_instance = ec2_resource.create_instances(**instance_params)
    
    # Get the instance ID of the newly created instance
    instance_id = new_instance[0].id
    
    return f"EC2 instance {instance_id} created successfully!"
