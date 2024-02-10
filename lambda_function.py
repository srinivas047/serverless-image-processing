import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['bucket']
    key = event['key']
    
    response = s3.get_object(Bucket=bucket_name, Key=key)
    img = Image.open(io.BytesIO(response['Body'].read()))
    img.thumbnail((200, 200))
    
    buffer = io.BytesIO()
    img.save(buffer, "JPEG")
    buffer.seek(0)
    
    new_key = f"resized-{key}"
    s3.put_object(Bucket=bucket_name, Key=new_key, Body=buffer, ContentType="image/jpeg")
    
    return {"statusCode": 200, "body": f"Resized image saved as {new_key}"}
