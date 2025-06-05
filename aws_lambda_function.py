import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
  '''
    When a lambda function is invoked, the runtime passes in 2 parameters:
    1. event - the event data (json), in this case, the S3 object that triggered the lambda function
    2. context - the lambda context with properties such as runtime environment, the function and the invocation
  '''


  #print("Received event: " + json.dumps(event, indent=2))

  # Get the object from the event and show its content type
  bucket = event['Records'][0]['s3']['bucket']['name']
  key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
  try:
      response = s3.get_object(Bucket=bucket, Key=key)
      print("CONTENT TYPE: " + response['ContentType'])
      return response['ContentType']
  except Exception as e:
      print(e)
      print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
      raise e