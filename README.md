# AWS Zero-Trust Cloud Firewall

> A serverless DevSecOps tool that enforces Zero-Trust architecture by automatically detecting and revoking unauthorized SSH access (Port 22) in real-time.

![AWS](https://img.shields.io/badge/AWS-Lambda-orange?style=for-the-badge&logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Zero%20Trust-red?style=for-the-badge)

## Architecture
This system operates on a **Detection & Response** loop:
1. **Trigger:** Amazon EventBridge schedules an audit every 1 hour.
2. **Audit:** AWS Lambda (Python/Boto3) scans all EC2 Security Groups.
3. **Logic:** Identifies rules allowing `0.0.0.0/0` on Port 22 (SSH).
4. **Remediation:** Instantly revokes the rule using the AWS API.

## Key Features
* **Automated Auditing:** Eliminates manual review of security groups.
* **Self-Healing Infrastructure:** Automatically reverts insecure changes.
* **Serverless:** Zero maintenance; runs on AWS Lambda.
* **Logging:** Full audit trail via Amazon CloudWatch.

## Technology Stack
* **Cloud:** AWS (Lambda, EC2, EventBridge, IAM)
* **Language:** Python 3.12
* **SDK:** Boto3

## How to Run Locally
1. Clone the repo
```bash
git clone [https://github.com/YOUR_USERNAME/aws-zero-trust-firewall.git](https://github.com/YOUR_USERNAME/aws-zero-trust-firewall.git)