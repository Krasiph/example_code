import boto3

def print_ec2_instances(access_key, secret_key, region):
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key,
                         region_name=region)

    for instance in ec2.instances.filter():
        print(instance.id, instance.instance_type)

    return
