# Repo: aws-intro-function
![Static Badge](https://img.shields.io/badge/Dev_status-Complete-blue)

## Reason: AWS Lambda Tutorial

### Description
This repo represents the Python code used in the AWS Lambda Function in the Youtube tutorial below.

View the tutoral here: [Create Your First AWS Lambda Function](https://www.youtube.com/watch?v=e1tkFsFOBHA)

### Tutorial Notes

- AWS Lambda - Event driven serverless computing.
- Events such as a change on a DB table row, or an entry into an S3 bucket will trigger the associated AWS Lambda Function.
- An AWS Lambda Function (such as the code in this repo) should have a single purpose to assure size/cost implications.

### The purpose of the tutorial was to:
- Upload a file to s3 (video, image, text file etc)
- This would cause the Lambda Function to trigger the event
- Which in turn outputs the content type to the log window

### AWS Console
- Navigate to S3 and create bucket
  - add bucket name (unique)
  - bucket needs to be in the same region as the Lambda Funciton
  - accept all defaults
  - create bucket
  - view details
- Navigate to Lambda
  - create new function
  - author from scratch
  - add function name
  - pick Runtime code (eg Python 3.13)
  - Permissions - Execution Role.
    -  create a new role from AWS policy templates
    -  give role a relevant name
    -  select template (Amazon S3 Read Only Permissions)
    -  create the function
- Function Editor
  - cut and paste code into the editor
  - click Deploy Code (and each time a change is made)
  - Scroll up to Add Trigger
    - Select the source (e.g. S3),
    - specifiy the Bucket
    - enter event type such as 'all create events'
    - acknowledge that using the same S3 bucket for input as output will cause an infinate loop and cause the cost implication of this
    - click Add


### Tech Stack/Dependencies:

- Python
- json
- urllib.parse
- boto3 - the S3 SDK for python
- AWS S3
- AWS Lambda

