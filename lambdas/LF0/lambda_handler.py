import json
import boto3

def handler(event, context):
  lexClient = boto3.client('lex-runtime')
  lexResponse = lexClient.post_text(
      botName='DiningConceirgeBot',
      botAlias='Dev',
      userId='comsw6998',
      inputText=event['messages'][0]['unstructured']['text']
    )
  response = {
    "messages": [
      {
        "type": "unstructured",
        "unstructured": {
          "id": 1,
          "text": lexResponse['message'],
          "timestamp": "14-02-2021"
        }
      }
    ]
  }
  return response
    
    
    