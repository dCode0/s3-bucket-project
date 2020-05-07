import boto3


def lambda_handler(event, context):
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket='mybucketname')['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][1]
    print(last_added)

    response = s3.delete_object(
        Bucket='mybucketname',
        Key=last_added,
    )

