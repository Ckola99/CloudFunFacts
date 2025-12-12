# ☁️ AWS Cloud FunFacts Generator
A serverless AWS project that generates fun cloud computing facts using:
- AWS Lambda
- DynamoDB
- API Gateway
- Python (boto3, AWS SDK)
- IAM
- AWS CLI

This project demonstrates real-world cloud engineering concepts including:
serverless compute, NoSQL data modeling, API design, IAM security, and automated data seeding.

---

## 🚀 Architecture Overview

```
User → API Gateway → Lambda Function → DynamoDB → Result to User
```

See `/infrastructure/architecture-diagram.txt` for the full diagram.

---

## 🌩️ Key AWS Services Used

| Service | Purpose |
|--------|---------|
| DynamoDB | Stores cloud fun facts |
| Lambda | Retrieves a random fact from DynamoDB |
| API Gateway | Exposes a REST endpoint for users |
| IAM | Controls access between Lambda and DynamoDB |
| AWS CLI | Used to seed the database |
| boto3 | Python SDK used in Lambda + seeding script |

---

## 📦 Project Structure

```
aws-cloud-funfacts/
│── lambda/
│── seed/
│── infrastructure/
```

---

## 🗄️ DynamoDB Table

- **Table name:** `CloudFunFacts`
- **Partition key:** `FactID` (String)

See `/infrastructure/dynamodb-table-definition.json`.

---

## 🧪 How to Seed the DynamoDB Table

### 1. Install dependencies
```bash
pip install boto3
```

### 2. Configure AWS CLI (if not done)
```bash
aws configure
```

### 3. Run the seed script
```bash
python seed/seed_dynamodb.py
```

You should see:
```
Successfully inserted all facts.
```

---

## 🧠 Lambda Function

Located in `/lambda/funfacts_lambda.py`.

The Lambda function:
1. Scans the DynamoDB table
2. Picks a random fact
3. Returns it through API Gateway

---

## 🌍 API Gateway Endpoint

The endpoint returns:
```json
{
  "FactID": "7",
  "FactText": "More than 90% of Fortune 100 companies use AWS."
}
```

Routes are stored in `/infrastructure/api-gateway-routes.txt`.
---

## 🧾 License

MIT License.
