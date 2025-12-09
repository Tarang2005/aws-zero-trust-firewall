# AWS Zero Trust Firewall – Automated Security Watcher

A Python-based automated AWS security enforcement tool that continuously monitors EC2 security groups and **removes unauthorized public access rules in real time** — demonstrating Zero Trust and DevSecOps automation.

---

## Features
- **Auto-Scan:** Automatically scans all EC2 Security Groups.
- **Detection:** Detects public exposure (`0.0.0.0/0`) on sensitive ports.
- **Remediation:** Removes unauthorized ingress rules instantly.
- **Logging:** Logs findings & remediation results.
- **Flexible:** Works locally or via AWS Lambda.
- **Continuous:** Supports real-time continuous monitoring.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python |
| **Cloud** | AWS |
| **Security** | EC2 Security Groups |
| **Automation** | Lambda + EventBridge |
| **Libraries** | `boto3` |

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/aws-zero-trust-firewall.git](https://github.com/YOUR_USERNAME/aws-zero-trust-firewall.git)
cd aws-zero-trust-firewall
```
### 2. Install dependencies
```
pip install boto3
```
### 3️. Run the watcher script
```
python src/watcher.py
```

Proof of Concept (Real Terminal Output)

<p align="center"> <img src="diagram/terminal.png" alt="Terminal Output" width="800"/> </p>

Deploy to AWS (Lambda)
Step	Action
1	Upload Python code to Lambda
2	Set Timeout → 15s
3	Add IAM role → AmazonEC2FullAccess
4	Add EventBridge Trigger → rate(5 minutes)
5	Verify logs via CloudWatch

Impact

Enforces Zero Trust
Reduces MTTR from days → seconds
Demonstrates AWS Security + DevSecOps Automation
Internship-ready real-world project

Contact
Author: Tarang Patra
LinkedIn: https://www.linkedin.com/in/tarang-patra-31072b2b2/
GitHub: https://github.com/Tarang2005
