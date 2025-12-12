import random
import json
import boto3

# Create DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudFacts')

# Bedrock client
bedrock = boto3.client("bedrock-runtime")
MODEL_ID = "openai.gpt-oss-120b-1:0"

def lambda_handler(event, context):
    # scan entire table only because of small dataset
    response = table.scan()
    items = response.get('Items', [])

    if not items:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"fact": "No facts available in DynamoDB."})
        }

    fact = random.choice(items)["FactText"]


     # Messages for AI model
    messages = [
        {
            "role": "user",
            "content": f"Take this cloud computing fact and make it fun and engaging in 1-2 sentences maximum. Keep it short and witty: {fact}"
        }
    ]

    body = {
        "messages": messages,
        "max_tokens": 100,
        "temperature": 0.7
    }

    try:
        bedrock_response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(body),
            contentType='application/json',
            accept='application/json'
        )

        result = json.loads(bedrock_response['body'].read())
        witty_fact= ""

        if "content" in result and result["content"]:
            for block in result["content"]:
                if block.get("type") == "text":
                    witty_fact = block["text"].strip()
                    break

        if not witty_fact or len(witty_fact) > 300:
            witty_fact = fact

    except Exception as e:
        print(f"Bedrock error: {e}")
        witty_fact = fact


    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({"fact": witty_fact})
    }
