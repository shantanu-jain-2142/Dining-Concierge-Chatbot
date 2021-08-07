import json
import boto3

def lambda_handler(event, context):
    sqsClient = boto3.client('sqs')
    sqsQueueUrl = 'https://sqs.us-east-1.amazonaws.com/025726486846/Dining_Conceirge_Queue'
    if event['currentIntent']['name'] == 'DiningSuggestionsIntent':
        identifiedSlots = event['currentIntent']['slots']
        messageAttributes = {
            'Cuisine': {
                'DataType': 'String',
                'StringValue': identifiedSlots['Cuisine']
            },
            'PhoneNumber': {
                'DataType': 'Number',
                'StringValue': identifiedSlots['Phone_number']
            },
            'NoOfPeople': {
                'DataType': 'Number',
                'StringValue': identifiedSlots['NumOfPeople']
            },
            'DiningTime': {
                'DataType': 'String',
                'StringValue': identifiedSlots['Dining_Time']
            },
            'Location': {
                'DataType': 'String',
                'StringValue': identifiedSlots['Location']
            },
            'Email': {
                'DataType': 'String',
                'StringValue': identifiedSlots['Email']
            }
            
        }
        response = sqsClient.send_message(QueueUrl=sqsQueueUrl, MessageBody="Message from Lex", MessageAttributes=messageAttributes)
        dialogAction = {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "Please give me a few minutes to find the perfect restaurant to your likings. I will send an SMS, once I am finished."
            }
        }
        return {"dialogAction": dialogAction}
    return {"message": "The intent matched might be wrong."}
    
    