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
