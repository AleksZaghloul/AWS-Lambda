# AWS-Lambda
Lambda code using boto3

From an AWS challenge lab, we were given a task to create an email alert with every upload to an S3 bucket, with no instructions on how to do so. This is my first time using Lambda and boto3.
First you have to create an S3 bucket, and an SNS topic. Make sure to place the correct topic arn and region in the code for it to work.
