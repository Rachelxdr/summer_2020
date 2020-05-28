import boto3

client = boto3.client('s3', region_name='us-west-2')

""" 
upload an image to an S3 bucket.
Bucket selection is hard coded at this point (su20).

params:
* path: The local path of the file to upload.
* name: The name of the file shown in S3 bucket.
"""


def upload_img(path, name):
    client.upload_file(path, 'su20', name)

