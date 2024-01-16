import json

def lambda_handler(event, context):
    # Extract integers from the event
    try:
        num1 = int(event['num1'])
        num2 = int(event['num2'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing required parameters: num1 and num2')
        }

    # Calculate the sum
    sum = num1 + num2

    # Return the result as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({'sum': sum})
    }