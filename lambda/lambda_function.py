import random
import json
import boto3
from botocore.exceptions import ClientError

# Global client initialization is good practice for performance
# DynamoDB Resource for simpler data handling
DYNAMODB_RESOURCE = boto3.resource('dynamodb')
TABLE_NAME = 'CloudFacts'
TABLE = DYNAMODB_RESOURCE.Table(TABLE_NAME)

# Bedrock client
BEDROCK_RUNTIME = boto3.client("bedrock-runtime")
MODEL_ID = "openai.gpt-oss-120b-1:0"

def lambda_handler(event, context):
    try:
        # 1. RETRIEVE FACT FROM DYNAMODB
        # Using the Resource.Table.scan() method
        response = TABLE.scan()
        items = response.get('Items', [])

        if not items:
            # Handle empty table case
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"fact": "No facts available in DynamoDB."})
            }

        # Select a random fact from the simpler Python dicts returned by the Resource
        fact = random.choice(items)["FactText"]

        # 2. PREPARE BEDROCK PAYLOAD (GPT-OSS/OpenAI Format)

        # Adding a system message gives the model better context and control
        messages = [
            {
                "role": "system",
                "content": "You are a cloud technology expert with a witty and enthusiastic personality. Your goal is to rewrite the user's fact to be fun, engaging, and surprising in 1-2 sentences maximum. Do not add external facts. Return ONLY the rewritten fact text."
            },
            {
                "role": "user",
                "content": f"Cloud computing fact to rewrite: {fact}"
            }
        ]

        body = {
            "messages": messages,
            "max_tokens": 100,
            "temperature": 0.8 # Bump up temperature slightly for more creativity
        }

        # 3. INVOKE BEDROCK
        bedrock_response = BEDROCK_RUNTIME.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(body),
            contentType='application/json',
            accept='application/json'
        )

        # 4. PARSE THE RESPONSE (CRITICAL FIX FOR GPT-OSS)
        result = json.loads(bedrock_response['body'].read())
        witty_fact = ""

        print(f"Bedrock response: {result}")  # Debugging line to inspect the full response

        # Check for the correct nested structure: choices[0].message.content
        if 'choices' in result and len(result['choices']) > 0:
            witty_fact = result['choices'][0]['message']['content'].strip()

        # 5. FALLBACK LOGIC
        # Use original fact if AI output is empty, too long, or parsing failed
        if not witty_fact or len(witty_fact) > 300:
            witty_fact = fact

    except ClientError as e:
        print(f"AWS Client Error: {e}")
        # Fallback to original fact on error
        witty_fact = fact

    except Exception as e:
        print(f"General Error: {e}")
        # Fallback to original fact on error
        witty_fact = fact

    # 6. RETURN FINAL API RESPONSE
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
