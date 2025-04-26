import boto3

hdhcdh
hdhhdhhd
def launch_ec2_instance():
    client = boto3.client('cloudformation')

    template_body = """
    AWSTemplateFormatVersion: '2010-09-09'
    Resources:
      MyEC2Instance:
        Type: 'AWS::EC2::Instance'
        Properties:
          InstanceType: t2.micro
          ImageId: ami-0abcdef1234567890  # Replace with a valid AMI ID
          KeyName: my-key-pair          # Replace with your key pair name
    """

    response = client.create_stack(
        StackName='MyEC2Stack',
        TemplateBody=template_body
    )

    return response

# Call the function to launch the EC2 instance
launch_ec2_instance()