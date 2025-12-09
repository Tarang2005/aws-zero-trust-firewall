# AWS Zero Trust Firewall – Automated Security Watcher

A Python-based automated AWS security enforcement tool that continuously monitors EC2 security groups and **removes unauthorized public access rules in real time** — demonstrating Zero Trust and DevSecOps automation.

---

## Features
- 🛡️ **Auto-Scan:** Automatically scans all EC2 Security Groups.
- 🚨 **Detection:** Detects public exposure (`0.0.0.0/0`) on sensitive ports.
- ⚡ **Remediation:** Removes unauthorized ingress rules instantly.
- 📝 **Logging:** Logs findings & remediation results.
- ☁️ **Flexible:** Works locally or via AWS Lambda.
- 🔄 **Continuous:** Supports real-time continuous monitoring.

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
2. Install dependenciesBashpip install boto3
3. Run the watcher scriptBashpython src/watcher.py
Proof of ConceptBelow is the real terminal output proving detection & automatic remediation:<p align="center"> <img src="diagram/terminal.png" alt="Terminal Output" width="800"/> </p>Deploy to AWS (Lambda)StepAction1Upload Python code to AWS Lambda.2Set Timeout → 15s.3Add IAM Role Permission → AmazonEC2FullAccess.4Add EventBridge Trigger → rate(5 minutes).5Verify logs via CloudWatch.Impact✅ Enforces Zero Trust: Removes implicit trust by verifying and closing open ports.✅ Speed: Reduces Mean Time to Remediate (MTTR) from days → seconds.✅ Automation: Demonstrates practical AWS Security + DevSecOps Automation.✅ Relevance: Internship-ready real-world project.ContactAuthor: Tarang PatraLinkedIn: Tarang PatraGitHub: Tarang2005
