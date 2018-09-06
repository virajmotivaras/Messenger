import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def NewMessage(event, context):
    statusMessage = "Message saved successfully!!!"

    #extract the message from the body of the message

    #store the message by  making call to DAL

    response = {
        "statusCode": 200,
        "body": json.dumps(statusMessage)
    }
    return response

def IsNewMessage(event, context):
    retVal = false
    # Check the db for new messages

    statusMessage = "Message Present: " + str(retVal)
    response = {
        "statusCode":200,
        "body": json.dumps(statusMessage)
    }

def GetNewMessage(event, context):

    msg = ''
    #read if there is a new message is waiting to be read
    statusMessage = "Message: " + msg
    response = {
        "statusCode":200,
        "body": json.dumps(statusMessage)
    }