import urllib.parse
import boto3
import io


s3 = boto3.client('s3')


def lambda_handler(event, context):

    TOPIC_ARN = #'arn:aws:sns:us-west-2:925597714900:WordCount' - paste your topic ARN
    REGION = 'us-west-2' #make sure you verify

    # Get the object from the event
    s3bucket = boto3.resource('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    #get the file based on key (name of file) and bucket name
    obj = s3bucket.Object(bucket, key)
    #read the contents and decode into text
    body = obj.get()['Body'].read().decode('utf-8')
    
    #Normal python - split by spaces into a list and count the length of list
    text_list = body.split()
    count = len(text_list)
    
    #connect to sns
    snsClient = boto3.client('sns', region_name=REGION)

    message = io.StringIO()
    message.write('The word count in the file {} is {}.'.format(key, count))
    #push message to topic, which will message you
    response = snsClient.publish(
    TopicArn = TOPIC_ARN,
    Subject = 'Word Count Result',
    Message = message.getvalue()
    )