#@author: Giten Mitra
#Date: 21 Nov 2022
#Description: This script will start EC2 instance on basic of Tag.

import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get region list
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

    # Iterating over region
    for region in regions:
        print("Region: ", region)
        ec2 = boto3.resource('ec2', region_name=region)

        # Filter instance based on Tag
        instances = ec2.instances.filter(
            Filters=[{'Name': 'tag:AutoSS', 'Values': ['Yes']}])

        # Iterate over instances
        try:
            for instance in instances:
                # Start the instance
                print("Starting the instance with instance-id: ", instance.id)
                instance.start()
        except Exception as e:
            print("Instance is already in start state: ",instance.id)
            print("Error is: ",e)