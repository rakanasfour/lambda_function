import json
import base64
import boto3  # Add this import statement
import string
import random

def lambda_handler(event, context):
    s3 = boto3.client("s3")

    # Check if 'httpMethod' key exists in the event dictionary
    if 'httpMethod' in event and event['httpMethod'] == 'OPTIONS':
        response_headers = {
            'Access-Control-Allow-Origin': '*',  # Adjust the origin as needed
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',  # Add OPTIONS method
        }
        response = {
            'statusCode': 200,
            'headers': response_headers,
        }
        return response

    get_file_content = event.get("body-json", "")
    decode_content = base64.b64decode(get_file_content)

    pic_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    s3_upload = s3.put_object(Bucket="dealership-us", Key=pic_filename + ".png", Body=decode_content)

    # TODO implement

    response_headers = {
        'Access-Control-Allow-Origin': '*',  # Adjust the origin as needed
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',  # Add OPTIONS method
    }

    response = {
        'statusCode': 200,
        'headers': response_headers,
        'body': json.dumps('The Object is Uploaded successfully!')
    }

    return response
