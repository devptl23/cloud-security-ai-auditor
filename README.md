# 🔐 AI-Powered Cloud Security Auditor

An automated cloud infrastructure security auditing system that combines Infrastructure-as-Code, API integration, and Generative AI to identify vulnerabilities and generate intelligent security recommendations.

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     YOUR LOCAL MACHINE                              │
│                                                                       │
│  ┌──────────────────┐                                               │
│  │  auditor.py      │◄─── Triggered by User                        │
│  │  (Python Script) │                                               │
│  └────────┬─────────┘                                               │
│           │                                                          │
│           ├─────────────────────┬──────────────────────┐           │
│           │                     │                      │           │
└───────────┼─────────────────────┼──────────────────────┼───────────┘
            │                     │                      │
            ▼                     ▼                      ▼
┌──────────────────────────────────────────────────────────────────────┐
│                         AWS CLOUD                                    │
│                                                                       │
│  ┌─────────────────────┐  ┌──────────────────┐  ┌──────────────┐  │
│  │   S3 Buckets       │  │  S3 API (boto3)  │  │  AWS Bedrock │  │
│  │                    │  │  Scans:          │  │  Generative  │  │
│  │ • secure-data     │  │  ✓ Encryption    │  │  AI Model    │  │
│  │ • vulnerable-data │  │  ✓ Public Access │  │              │  │
│  │                    │  │  ✓ Logging       │  │ Titan Text   │  │
│  │                    │  │  ✓ Versioning    │  │ Express      │  │
│  └────────┬───────────┘  └────────┬─────────┘  └──────┬───────┘  │
│           │                        │                     │          │
│           └────────────────────────┼─────────────────────┘          │
│                                    │                                │
│                            ┌───────▼────────┐                      │
│                            │  Security Data │                      │
│                            │  Analysis      │                      │
│                            └────────┬───────┘                      │
│                                     │                              │
└─────────────────────────────────────┼──────────────────────────────┘
                                      │
                    ┌─────────────────▼─────────────┐
                    │  AI-Generated Report          │
                    │  • Security Issues            │
                    │  • Compliance Status          │
                    │  • Recommendations            │
                    └───────────────────────────────┘
```

---

## 📋 How It Works

1. **Infrastructure Provisioning** (Terraform)
   - Deploys AWS S3 buckets as test infrastructure
   - Demonstrates IaC best practices

2. **Security Scanning** (Python + boto3)
   - Connects to your AWS account
   - Scans S3 bucket configurations
   - Collects security metrics:
     - Encryption status
     - Public access controls
     - Versioning settings
     - Access logging configuration

3. **AI Analysis** (AWS Bedrock)
   - Sends security data to generative AI
   - AI identifies vulnerabilities
   - Generates actionable recommendations
   - Produces compliance report

4. **Output**
   - Professional security audit report
   - Ready for LinkedIn/portfolio showcase

---

## ✨ Features

- ✅ **Automated Infrastructure Deployment** - Terraform IaC for reproducible infrastructure
- ✅ **Real-time Security Scanning** - Python AWS API integration
- ✅ **AI-Powered Analysis** - AWS Bedrock generative AI for intelligent recommendations
- ✅ **Professional Reports** - Formatted security audit output
- ✅ **Zero Charge** - Fully automated cleanup (terraform destroy)
- ✅ **Portfolio Ready** - Complete project for recruiters

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Infrastructure | **Terraform** | Deploy AWS S3 buckets (IaC) |
| Automation | **Python 3** | Orchestrate scanning and analysis |
| Cloud APIs | **boto3** | AWS SDK for S3 interaction |
| Generative AI | **AWS Bedrock** | Intelligent security recommendations |
| Deployment | **AWS** | Cloud infrastructure |

---

## 📦 Project Structure

```
cloud-security-auditor-ai/
├── main.tf                 # Terraform configuration for S3 buckets
├── auditor.py             # Python script for security auditing
├── terraform.tfstate      # Terraform state file (empty after destroy)
├── .gitignore             # Security - prevents credential commits
└── README.md              # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites
- AWS Account with credentials configured
- Terraform installed
- Python 3.8+
- AWS CLI configured (`aws configure`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cloud-security-auditor-ai.git
   cd cloud-security-auditor-ai
   ```

2. **Configure AWS Credentials**
   ```bash
   aws configure
   # Enter: Access Key ID
   # Enter: Secret Access Key
   # Enter: Region (us-east-1)
   # Enter: Output format (json)
   ```

3. **Deploy Infrastructure**
   ```bash
   terraform init
   terraform plan
   terraform apply
   # Type 'yes' when prompted
   ```

4. **Install Python Dependencies**
   ```bash
   pip install boto3
   ```

5. **Run the Auditor**
   ```bash
   python auditor.py
   ```

6. **Expected Output**
   ```
   Checking buckets...
   
   ============================================================
   🔐 AI-POWERED CLOUD SECURITY AUDIT REPORT
   ============================================================
   
   1. Identified Security Issues:
   - The S3 bucket is publicly accessible
   - The S3 bucket has no encryption at rest
   - The S3 bucket has no access logging enabled
   ...
   
   ============================================================
   ```

7. **Clean Up** (Important to avoid charges!)
   ```bash
   terraform destroy
   # Type 'yes' when prompted
   ```

---

## 📊 Security Checks Performed

The auditor evaluates:

| Check | Purpose | Risk Level |
|-------|---------|-----------|
| **Encryption** | Data at rest protection | 🔴 High |
| **Public Access** | Unauthorized access prevention | 🔴 High |
| **Versioning** | Data recovery capability | 🟡 Medium |
| **Access Logging** | Compliance & forensics | 🟡 Medium |

---

## 🧠 Key Learnings

This project demonstrates:

- **Infrastructure as Code** - Reproducible infrastructure using Terraform
- **Cloud API Integration** - Working with AWS services programmatically
- **Generative AI Integration** - Leveraging LLMs for intelligent analysis
- **DevSecOps** - Security-first cloud infrastructure practices
- **Python Automation** - Building cloud automation scripts
- **AWS Best Practices** - Proper credential management, cleanup, cost control

---

## 💡 Why This Project Matters

For **Recruiters & Hiring Managers**, this demonstrates:

1. **Full-Stack Cloud Engineering** - IaC → API Integration → AI
2. **Security Mindset** - Understanding cloud security fundamentals
3. **AI/ML Adoption** - Leveraging cutting-edge generative AI
4. **DevOps Maturity** - Automation and infrastructure management
5. **Practical Problem-Solving** - Real security auditing use case

---

## 🔒 Security Considerations

- ✅ `.gitignore` prevents credential leaks
- ✅ No hardcoded AWS keys in code
- ✅ terraform.tfstate cleaned up after destroy
- ✅ All resources destroyed to prevent unexpected charges
- ✅ IAM principle of least privilege recommended

---

## 📈 Next Steps / Enhancements

- [ ] Add multi-region scanning
- [ ] Create CloudWatch integration
- [ ] Build web dashboard for reports
- [ ] Add automated remediation capabilities
- [ ] Support for other AWS services (EC2, RDS, etc.)
- [ ] Cost optimization analysis

---

## 🤝 Contributing

Have improvements? Feel free to fork and submit a PR!

---

## 📄 License

MIT License - Feel free to use this project for learning and portfolio purposes.

---

## 📞 Questions?

Check out the [AWS Security Best Practices](https://docs.aws.amazon.com/security/) and [Terraform Documentation](https://www.terraform.io/docs).

---

**⭐ If this project helped you, please star it on GitHub!**

Built with ❤️ for cloud security and AI enthusiasts.
