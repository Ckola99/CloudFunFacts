import subprocess
import json
import os


TABLE_DEFINITION_PATH = "infrastructure/dynamodb-table-definition.json"


def create_dynamodb_table():
    """Runs the AWS CLI command to create the DynamoDB table."""

    # Check if the definition file exists
    if not os.path.exists(TABLE_DEFINITION_PATH):
        print(f"❌ Error: Table definition file not found at {TABLE_DEFINITION_PATH}")
        return

    print(f"Starting DynamoDB table creation using definition file: {TABLE_DEFINITION_PATH}")

    # Construct the full CLI command
    command = [
        "aws",
        "dynamodb",
        "create-table",
        f"--cli-input-json",
        f"file://{TABLE_DEFINITION_PATH}"
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(
            command,
            check=True,  # This raises an error if the command fails
            capture_output=True,
            text=True
        )

        # Parse the JSON response for cleaner output
        response = json.loads(result.stdout)
        table_name = response['TableDescription']['TableName']
        table_status = response['TableDescription']['TableStatus']

        print(f"   Success: Table '{table_name}' creation initiated.")
        print(f"   Initial Status: {table_status}")

    except subprocess.CalledProcessError as e:
        print(f"   CLI Error (Return Code {e.returncode}):")
        print(f"   STDOUT: {e.stdout.strip()}")
        print(f"   STDERR: {e.stderr.strip()}")
    except FileNotFoundError:
        print("   Error: 'aws' command not found. Ensure the AWS CLI is installed and in your PATH.")
    except Exception as e:
        print(f"  An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_dynamodb_table()
