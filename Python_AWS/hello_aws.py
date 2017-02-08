import boto3
import argparse


def print_ec2_instances(access_key, secret_key, region):
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key,
                         region_name=region)

    for instance in ec2.instances.filter():
        name = 'Unknown'
        status = 'Normal'
        
        for tag in instance.tags:
            if tag['Key'] == 'Name':
                name = tag['Value']
            
            elif tag['Key'] == 'Status':
                status = tag['Value']
        
        print('Name: {0}\n\tInstance ID: {1}\n\tInstance Type: {2}\n\tStatus: {3}\n'.format(name,
                                                                                            instance.id,
                                                                                            instance.instance_type,
                                                                                            status))

    return


def launch_ec2_instances(access_key, secret_key, region, how_many=1):
    ec2 = boto3.resource('ec2',
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key,
                         region_name=region)

    ec2.create_instances(ImageId='ami-65b13405',
                         MinCount=1,
                         MaxCount=how_many,
                         KeyName='adcrush_farming',
                         InstanceType='t2.micro',
                         SecurityGroupIds=['sg-66ad641e'],
                         InstanceInitiatedShutdownBehavior='stop')

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a simple AWS API example')
    
    parser.add_argument('access_key', help='the access key for the Python account')
    parser.add_argument('secret_key', help='the secret key for the Python account')
    parser.add_argument('-c', '--command', default='status', help='the command to run (launch, status)')
    parser.add_argument('-n', '--number_to_launch',
                        default=1, type=int,
                        help='the number of instances to launch with the launch command')
    parser.add_argument('-r', '--region', default='us-west-2', help='the region to access')
    
    args = parser.parse_args()

    if args.command == 'launch':
        launch_ec2_instances(args.access_key,
                             args.secret_key,
                             args.region,
                             args.number_to_launch)

    elif args.command == 'status':
        print_ec2_instances(args.access_key,
                            args.secret_key,
                            args.region)
