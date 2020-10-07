# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# Licensed under the MIT License. See the LICENSE accompanying this file
# for the specific language governing permissions and limitations under
# the License.
import json
import boto3

def lambda_handler(event, context):

    try:
        
        print('******* Event body *******', event['body'])
        
        # calling Custom Comprehend Named entity recognition API in real time
        # to fetch product and its version details from the email message body
        client_Comp = boto3.client('comprehend', region_name='<YOUR REGION>')
        response_Entity = client_Comp.detect_entities(
        EndpointArn="<YOUR ENDPOINT ARN>",
        LanguageCode="en",
        Text=event['body']
        )
        
        print('******* response Object 1 *******', response_Entity['Entities'][0]['Text'])
        print('******* response Object 2 *******', response_Entity['Entities'][1]['Text'])
        
        # generating response
        responseBody = {
            'service': response_Entity['Entities'][0]['Text'],
            'version': response_Entity['Entities'][1]['Text'],
            'input': event
        }
        
        response = json.dumps(responseBody)
        
    
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        'statusCode': 200,
        'body': response
    }
