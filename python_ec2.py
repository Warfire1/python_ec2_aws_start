import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId="ami-0aa7d40e",
    MinCount=1,
    MaxCount=1,
    InstanceType="t1.micro",
    KeyName="KeyPair2",
    SubnetId="subnet-0e519b8"
)
