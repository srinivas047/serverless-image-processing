# Serverless Image Processing
A serverless application that resizes images using AWS Lambda and S3.

## Features
- Automatically resizes uploaded images.
- Supports API Gateway for integration.

## Setup
1. Deploy Lambda function and set up API Gateway.
2. Configure the S3 bucket using `s3_bucket_setup.yml`.
3. Test the app using `tests/test_lambda.py`.
