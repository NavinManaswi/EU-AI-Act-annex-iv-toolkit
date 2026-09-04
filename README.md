# 🇪🇺 EU AI Act Annex IV Technical Documentation Toolkit

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Compliant-green.svg)]()
[![Annex IV](https://img.shields.io/badge/Annex%20IV-Ready-blue.svg)]()

---

## 📋 Table of Contents

- [About This Toolkit](#-about-this-toolkit)
- [What Is Annex IV?](#-what-is-annex-iv)
- [Repository Structure](#-repository-structure)
- [How to Use This Toolkit](#-how-to-use-this-toolkit)
- [Example: CreditIQ Annex IV](#-example-creditiq-annex-iv)
- [Regulatory Mapping](#-regulatory-mapping)
- [Contact](#-contact)
- [License](#-license)

---

## 🎯 About This Toolkit

This repository contains a **complete, production-ready toolkit** for creating EU AI Act Annex IV Technical Documentation—the mandatory documentation required for high-risk AI systems under the EU AI Act.

The toolkit demonstrates:

- ✅ **All 9 Annex IV Sections** — Complete templates for every required section
- ✅ **Filled Example (CreditIQ)** — A real-world example for a financial services AI system
- ✅ **Readiness Checklist** — Step-by-step audit preparation guide
- ✅ **Automation Scripts** — CLI tools to scaffold and validate documentation
- ✅ **CI/CD Integration** — GitHub Actions workflow for continuous compliance validation

**Organization:** NovaTech Financial Group *(hypothetical)*  
**Effective Date:** 15 August 2026  
**Compliance Target:** Q4 2026

---

## 📖 What Is Annex IV?

**Annex IV of the EU AI Act** specifies the **technical documentation** that providers of high-risk AI systems must prepare before placing their systems on the market.

| Article | Requirement | Annex IV Section |
|---------|-------------|------------------|
| Art. 11 | Technical Documentation | All sections |
| Art. 9 | Risk Management System | Section 4 |
| Art. 10 | Data Governance | Section 2 |
| Art. 13 | Transparency | Section 6 |
| Art. 14 | Human Oversight | Section 6 |
| Art. 15 | Accuracy, Robustness, Cybersecurity | Sections 5, 7 |

> **⚠️ The Compliance Mirage:** Enforcement powers went live on 2 August 2026. The compliance deadlines for high-risk systems were pushed to 2 December 2027—but enforcement actions are already happening. *Organizations that wait will scramble.*

---

## 📂 Repository Structure

eu-ai-act-annex-iv-toolkit/

├── annex-iv-sections/ # Section-by-section templates

│ ├── 01-system-description.md

│ ├── 02-data-governance.md

│ ├── 03-technical-architecture.md

│ ├── 04-risk-management.md

│ ├── 05-performance-metrics.md

│ ├── 06-human-oversight.md

│ ├── 07-cybersecurity.md

│ ├── 08-post-market-monitoring.md

│ └── 09-conformity-assessment.md

├── templates/

│ └── annex-iv-template.md # Complete fillable template

├── examples/

│ └── creditiq-annex-iv.md # Filled example for CreditIQ

├── checklists/

│ └── annex-iv-readiness-checklist.md

├── scripts/

│ ├── generate-annex-iv.py # Scaffold new Annex IV docs

│ └── validate-annex-iv.py # Validate completeness

└── .github/workflows/

└── validate-annex-iv.yml # CI/CD compliance check



---

## 🚀 How to Use This Toolkit

| Step | Action | Description |
|------|--------|-------------|
| **1** | Start with the template | Use `templates/annex-iv-template.md` as your base |
| **2** | Follow the sections | Complete each section in `annex-iv-sections/` with your system's details |
| **3** | Reference the example | Check `examples/creditiq-annex-iv.md` for a real-world example |
| **4** | Run validation | Use `scripts/validate-annex-iv.py` to check completeness |
| **5** | Prepare for audit | Use `checklists/annex-iv-readiness-checklist.md` to ensure audit readiness |

---

## 🏆 Example: CreditIQ Annex IV

The `examples/creditiq-annex-iv.md` file contains a fully completed Annex IV documentation package for **CreditIQ**—an automated credit underwriting system processing 2.4 million applications annually.

**Key Highlights:**

| Section | Content |
|---------|---------|
| **1. System Description** | XGBoost classifier; fully automated for 85% of decisions |
| **2. Data Governance** | 4.2M training records; proxy risk identified; bias mitigation implemented |
| **4. Risk Management** | 7 identified risks; mitigation plans; residual risk accepted |
| **5. Performance Metrics** | AUC 0.82; DIR 74% → 86% (after remediation) |

---

## 🔗 Regulatory Mapping

| EU AI Act Article | Annex IV Section | Toolkit Artifact |
|-------------------|------------------|------------------|
| **Art. 9** — Risk Management | Section 4 | `annex-iv-sections/04-risk-management.md` |
| **Art. 10** — Data Governance | Section 2 | `annex-iv-sections/02-data-governance.md` |
| **Art. 11** — Technical Documentation | All sections | All artifacts |
| **Art. 12** — Record-Keeping | Section 8 | `annex-iv-sections/08-post-market-monitoring.md` |
| **Art. 13** — Transparency | Section 6 | `annex-iv-sections/06-human-oversight.md` |
| **Art. 14** — Human Oversight | Section 6 | `annex-iv-sections/06-human-oversight.md` |
| **Art. 15** — Accuracy & Robustness | Section 5, 7 | `annex-iv-sections/05-performance-metrics.md` |
| **Art. 16** — Conformity Assessment | Section 9 | `annex-iv-sections/09-conformity-assessment.md` |

---

## 📫 Contact

| Channel | Details |
|---------|---------|
| **GitHub** | [github.com/NavinManaswi](https://github.com/NavinManaswi) |
| **LinkedIn** | [linkedin.com/in/NavinManaswi](https://linkedin.com/in/NavinManaswi) |
| **Email** | manaswink@gmail.com |

---

## 📝 License

This toolkit is licensed under the **MIT License**. You are free to use, modify, and distribute the artifacts with attribution.

---

## ⭐ Star This Repository

If you find this toolkit helpful, please **star** this repository and share it with your network!
