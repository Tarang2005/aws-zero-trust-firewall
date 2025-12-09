# AWS Zero-Trust Cloud Firewall

> A serverless DevSecOps tool that enforces Zero-Trust architecture by automatically detecting and revoking unauthorized SSH access (Port 22) in real-time.

![AWS](https://img.shields.io/badge/AWS-Lambda-orange?style=for-the-badge&logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Zero%20Trust-red?style=for-the-badge)

---

## Architecture
This system operates on a **Detection & Response** cycle:

1. **Trigger:** Amazon EventBridge schedules an audit every 1 hour.
2. **Audit:** AWS Lambda (Python/Boto3) scans all EC2 Security Groups.
3. **Logic:** Identifies rules allowing `0.0.0.0/0` on Port 22 (SSH).
4. **Remediation:** Instantly revokes the rule using the AWS API.

*Architecture diagram located in:* `diagrams/architecture.png`

---

## Key Features
- **Automated Auditing:** Eliminates manual review of security groups.
- **Self-Healing Infrastructure:** Automatically reverts insecure changes.
- **Serverless:** Zero maintenance; runs entirely on AWS Lambda.
- **Logging:** Full audit trail via Amazon CloudWatch.

---

## Technology Stack
| Category | Tools |
|----------|-------|
| Cloud | AWS (Lambda, EC2, EventBridge, IAM, CloudWatch) |
| Language | Python 3.12 |
| Library | Boto3 |

---

## How to Run Locally
1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/aws-zero-trust-firewall.git
cd aws-zero-trust-firewall
Install dependencies

bash
Copy code
pip install boto3
Run the watcher script

bash
Copy code
python src/watcher.py

Proof of Concept
Terminal output demonstrating real detection & auto-remediation:


mathematica
Copy code
ALERT: Found Open Port 22 in sg-077000ff...
ACTION TAKEN: Removed public SSH access for sg-077000ff...
Scan Complete — Fixed 1 security risks.
Deployment (AWS)
Deploy Python code to AWS Lambda

Set Lambda Timeout → 15 seconds

Attach IAM Role → AmazonEC2FullAccess

Create EventBridge rule → rate(1 hour)

Validate results through CloudWatch Logs

Impact
Reduced MTTR from days → seconds

Enforced Zero-Trust cloud governance

Demonstrated DevSecOps + Automation + AWS Security

Contact
Author: YOUR NAME
LinkedIn: https://www.linkedin.com/in/tarang-patra-31072b2b2/
GitHub: https://github.com/Tarang2005
