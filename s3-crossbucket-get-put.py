import boto3
import os


def lambda_handler(event, contaxt):
     bucket = os.environ["bucket"]
     bucket1 = os.environ["bucket1"]
     filename = os.environ["filename"]
     prefix = os.environ['prefix']

     s3 = boto3.resource('s3')
     client = boto3.client('s3')

     response = client.list_objects(
          Bucket=bucket1,
          Prefix=prefix,
     )
     obj = response['Contents'][1]['Key']

     responseobj = client.get_object(Bucket=bucket1, Key=obj)

     data1 = responseobj['Body'].read().decode("utf-8")
     print(data1)

     response1 = client.put_object(
          Body=data1,
          Bucket=bucket,
          Key=filename, )
