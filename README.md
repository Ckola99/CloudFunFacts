# 🌩️ AWS Cloud FunFacts Generator

A fully serverless cloud application built using **AWS Lambda**, **API Gateway**, **DynamoDB**, and **AWS Bedrock AI**, designed to deliver fun cloud computing facts through a fast, cost-effective, scalable architecture.

🔗 **Live App:** https://production.d11q6mprl0gz9y.amplifyapp.com/

---

## 🏗️ Overview

This project demonstrates real-world AWS workflows including:

- Event-driven compute with Lambda
- NoSQL design with DynamoDB
- REST API creation with API Gateway
- AI-powered functionality with Bedrock
- AWS CLI + boto3 automation
- IAM access control and security
- Web deployment with Amplify Hosting

---

## 🧠 What I Learned

### ✔ Serverless Architecture
Understanding how Lambda executes code without servers, scales automatically, and integrates cleanly with other AWS services. This included working with cold starts, permissions, environment variables, and debugging runtime errors.

### ✔ API Gateway
Designed an HTTP API to route user requests to Lambda with focus on:

- CORS configuration
- Lambda proxy integrations
- API error handling
- Testing endpoints

### ✔ DynamoDB
Hands-on experience with NoSQL modeling and table design:

- Partition keys (FactID)
- Efficient read-based workflows
- Batch writes with `batch_writer()`
- IAM restrictions and troubleshooting
- Table creation via CLI and scripts

### ✔ AWS CLI & boto3
Scripted infrastructure processes using Python and the AWS CLI, including:

- Table creation
- Batch data seeding
- JSON-based data models

### ✔ AWS Bedrock AI
Experimented with Bedrock models for generating cloud facts. Initially tried OpenAI, which returned full reasoning traces. Wrote a **regex filter** to remove noise and return clean responses, then switched to Bedrock for smoother AWS-native integration.

### ✔ IAM & Security
Debugging IAM errors provided real-world experience with:

- Identity-based vs resource policies
- Role assumptions
- The Principle of Least Privilege
- Cloud permission troubleshooting

---

## ⚙️ Architecture

```
User → API Gateway → Lambda → DynamoDB → (Optional AI: Bedrock)
```
## 📊 Architecture Diagram
![Cloud Fun Facts Architecture](infrastructure/architecture-diagram.png)

### Why this stack?

**Lambda:**
- No servers to manage
- Auto-scaling
- Extremely cost-effective
- Perfect for micro-APIs

**API Gateway:**
- Secure API hosting
- Native Lambda integration
- Handles routing + response formatting

**DynamoDB:**
- Single-digit ms read times
- Serverless
- Great for key/value lookups

**Bedrock:**
- AWS-native model hosting
- Private & secure
- Clean JSON outputs

---

## 📦 Project Structure

```
CloudFunFacts/
│── lambda/
│   ├── lambda_function.py
│   └── requirements.txt
│
│── seed/
│   ├── funfacts.json
│   └── seed_dynamodb.py
│
│── infrastructure/
│   ├── api-gateway-routes.txt
│   ├── architecture-diagram.txt
│   └── dynamodb-table-definition.json
│
│── scripts/
│   └── create_table.sh
│
│── tests/
│   └── test_api.py
│
│── index.html
│── manage_infrastructure.py
│── README.md
│── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- AWS Account
- AWS CLI configured
- Python 3.x
- boto3 installed

### 1️⃣ Install Dependencies

```bash
pip install boto3
```

### 2️⃣ Configure AWS CLI

```bash
aws configure
```

### 3️⃣ Seed the DynamoDB Table

```bash
python seed/seed_dynamodb.py
```

---

## 🗄️ DynamoDB Setup

The DynamoDB table uses a simple schema:
- **Primary Key:** FactID (String)
- **Attributes:** FactText (String)

---

## 🧠 Lambda Function

Located in `/lambda/lambda_function.py`.

The function:
1. Scans the DynamoDB table
2. Selects a random fact
3. Returns the result via API Gateway

Fast and fully serverless.

---

## 🌍 REST API Response Example

```json
{
  "FactID": "7",
  "FactText": "More than 90% of Fortune 100 companies use AWS."
}
```

---

## 🏁 Key Takeaways

This project provided practical experience with:

- Designing real serverless systems
- Debugging IAM permissions
- Automating infrastructure
- Using DynamoDB and Lambda together
- Integrating AI with Bedrock
- Deploying a production-ready workflow

---

## 📜 License

MIT License

---

## 🤝 Connect

Feel free to reach out or contribute to this project!

**Live Demo:** https://production.d11q6mprl0gz9y.amplifyapp.com/
