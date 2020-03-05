import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    transactionId = event['queryStringParameters']['transactionId']
    
    s3Client = boto3.client('s3')
    
    bucketResponse = s3Client.list_buckets()
    print(bucketResponse)
    #print(type(bucketResponse['Buckets']['Name']))
    
    transactionRespone = {}
    
    responseObject = {}
    
    if bucketResponse == {}:
        transactionRespone['transId'] = transactionId
        transactionRespone['message']="there are no buckets created in s3"
        responseObject['statusCode'] = 200
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['body'] = json.dumps(transactionRespone)
    else:
      #  transactionRespone['transId'] = transactionId
       # transactionRespone['message'] = bucketResponse
        responseObject['statusCode'] = 200
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['body'] = json.dumps(bucketResponse, indent=4, sort_keys=True, default=str)
    
    return responseObject