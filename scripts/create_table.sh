#!/bin/bash

# Define the path to your table definition file
TABLE_DEFINITION_FILE="infrastructure/dynamodb-table-definition.json"


echo "Starting DynamoDB table creation using definition file: $TABLE_DEFINITION_FILE"

# Run the AWS CLI command to create the table
aws dynamodb create-table --cli-input-json file://"$TABLE_DEFINITION_FILE"

# Check the exit status of the previous command
if [ $? -eq 0 ]; then
    echo "Success: DynamoDB table creation initiated."
    echo "Note: The table is likely in 'CREATING' status. Check the AWS console for confirmation."
else
    echo "❌ Error: Failed to initiate table creation. Check your AWS CLI configuration and JSON file syntax."
fi
