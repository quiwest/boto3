import boto3

DryRun = True
ec2_client = boto3.client('ec2')
images = ec2_client.describe_images(
  Filters=[
        {
            'Name': 'name',
            'Values': [
                'amzn2-ami-hvm*',
            ]
        },
        {
            'Name': 'owner-alias',
            'Values': [
                'amazon',
            ]
        },
    ],
)
imageId = images['Images'][0]['ImageId']
print(imageId)
instance = ec2_client.run_instances(
  ImageId=imageId,
  InstanceType='t2.micro',
  MaxCount=1,
  MinCount=1,

  DryRun=DryRun
)
print(instance)
