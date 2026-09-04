---
title: EU AI Act Annex IV Technical Documentation
document_id: ANNEX-IV-CIQ-2026-001
version: 1.0
date: 15 August 2026
system_name: CreditIQ
provider: NovaTech Financial Group
---

# Annex IV Technical Documentation — CreditIQ

**Provider:** NovaTech Financial Group  
**Date:** 15 August 2026  
**Version:** 1.0  
**Document ID:** ANNEX-IV-CIQ-2026-001

---

## 📋 Table of Contents

1. [System Description](#1-system-description)
2. [Data Governance](#2-data-governance)
3. [Technical Architecture](#3-technical-architecture)
4. [Risk Management](#4-risk-management)
5. [Performance Metrics](#5-performance-metrics)
6. [Human Oversight](#6-human-oversight)
7. [Cybersecurity](#7-cybersecurity)
8. [Post-Market Monitoring](#8-post-market-monitoring)
9. [Conformity Assessment](#9-conformity-assessment)

---

## 1. System Description

### 1.1 General Description

| Attribute | Detail |
|-----------|--------|
| **System Name** | CreditIQ v4.2 |
| **System Type** | Predictive AI (Supervised Classification) |
| **Model Architecture** | XGBoost Classifier (Ensemble of Decision Trees) |
| **Intended Purpose** | Automate initial creditworthiness scoring and decisioning for unsecured personal loans up to $50,000 |
| **Decision Authority** | Fully automated for scores > 720 and < 580; Human-in-the-loop for scores 580-720 |
| **Deployment Jurisdictions** | USA (Federal + NY, CO, CA), UK (FCA), EU (Ireland & Germany) |
| **Affected Population** | ~2.4 million annual loan applicants |

### 1.2 Intended Use

CreditIQ is designed to provide credit decisions for unsecured personal loans. It is used by NovaTech's retail lending division to:

- Assess creditworthiness based on 85 financial and demographic features
- Provide immediate approval or rejection decisions
- Generate explanations for adverse action notices

### 1.3 System Boundaries

CreditIQ **does not**:

- Make decisions on secured loans (mortgages, auto loans)
- Process applications from non-EU residents outside the US/UK
- Make decisions without human oversight for borderline cases (scores 580-720)

---

## 2. Data Governance

### 2.1 Training Data Overview

| Attribute | Detail |
|-----------|--------|
| **Source** | NovaTech historical loan portfolio (2010-2022) |
| **Volume** | 4.2 million applications |
| **Features** | 85 features (credit bureau scores, DTI ratio, employment length, income stability, housing status, past delinquencies) |
| **Protected Attributes** | Explicitly Excluded: Race, gender, ethnicity, religion, sexual orientation |
| **Proxy Risk Identified** | Geographic zip codes and certain employment sectors identified as potential proxies for race/ethnicity |
| **Data Privacy Classification** | PII / Personal Financial Data (Subject to GDPR/CCPA) |

### 2.2 Data Quality Controls

| Control | Implementation | Owner |
|---------|----------------|-------|
| **Data Validation** | Automated checks for nulls, outliers, and data type mismatches | Data Engineer |
| **Data Freshness** | Monthly refresh of bureau data and economic indicators | Data Ops |
| **Data Retention** | GDPR-compliant deletion of personal data after 7 years | Data Privacy Officer |
| **Access Controls** | Role-based access; audit logging of all data queries | Security Team |

### 2.3 Data Privacy

All data is encrypted at rest and in transit. Data processing is documented in a GDPR Article 30 Record of Processing Activities. Data subject rights (access, correction, deletion, restriction) are supported through a centralized privacy portal.

---

## 3. Technical Architecture

### 3.1 Architecture Overview

CreditIQ follows a cloud-native architecture with the following components:

1. **Data Ingestion Layer** — Collects credit bureau data, internal banking data, and economic indicators
2. **Feature Engineering Pipeline** — Transforms raw data into 85 model features
3. **Model Inference Engine** — XGBoost model running in Azure ML
4. **Decision Engine** — Applies decision thresholds and generates outputs
5. **Explainability Layer** — LIME (Local Interpretable Model-agnostic Explanations) for borderline cases
6. **Monitoring Layer** — Continuous performance and drift monitoring

### 3.2 Data Flow Diagram
[Credit Bureau APIs] ─┐
[Internal Banking DB] ─┼─→ [Data Lake (Encrypted)]
[Economic Indicators] ─┘ ↓
[Feature Engineering Pipeline]
↓
[XGBoost Model Inference]
↓
[Decision Engine (Thresholds)]
↓
┌───────────┼───────────┐
↓ ↓ ↓
[Auto-Approval] [Review] [Auto-Rejection]
↓
[LIME Explanation Layer]
↓
[Plain-Language Adverse Action Notice]


### 3.3 Infrastructure

| Component | Detail |
|-----------|--------|
| **Deployment** | Azure Cloud (EU-West, US-East, US-West) |
| **Model Registry** | MLflow |
| **API** | REST API with rate limiting (1000 requests/minute) |
| **Monitoring** | Azure Monitor + Prometheus metrics |
| **Disaster Recovery** | Multi-region failover within 5 minutes |

---

## 4. Risk Management

### 4.1 Risk Identification

| Risk ID | Description | Category | Inherent Risk |
|---------|-------------|----------|---------------|
| CIQ-R01 | Algorithmic bias — disparate impact across racial groups | Fairness / Bias | Critical |
| CIQ-R02 | Unexplainable outputs — ECOA compliance risk | Explainability | High |
| CIQ-R03 | Economic drift — model instability during recessions | Reliability | High |
| CIQ-R04 | Adversarial tampering — fraud vulnerability | Security | Medium |
| CIQ-R05 | Regulatory breach — EU AI Act non-compliance | Legal/Compliance | High |
| CIQ-R06 | Data privacy breach — unauthorized access to PII | Privacy | High |
| CIQ-R07 | Cascading failure — manual fallback overwhelmed | Resilience | High |

### 4.2 Risk Analysis

| Risk ID | Likelihood | Impact | Control | Residual Risk |
|---------|------------|--------|---------|---------------|
| CIQ-R01 | High | Critical | Pre-processing bias mitigation; quarterly third-party audits | Medium |
| CIQ-R02 | Medium | High | LIME explanations; human review for borderline cases | Medium |
| CIQ-R03 | High | High | Weekly monitoring; automatic tempering at 0.2 PSI | Medium |
| CIQ-R04 | Low | Medium | Rate limiting; anomaly detection | Low |
| CIQ-R05 | Medium | High | Annex IV documentation; mock regulatory inspections | Medium |
| CIQ-R06 | Medium | High | Differential privacy; enhanced audit logging | Low |
| CIQ-R07 | Low | High | Cross-trained underwriters; capacity planning | Medium |

### 4.3 Risk Treatment

| Risk ID | Treatment Decision | Treatment Plan | Owner | Target Date |
|---------|-------------------|----------------|-------|-------------|
| CIQ-R01 | Mitigate | Reweight training samples; hard fairness constraint; quarterly third-party audits | Head of Model Validation | 15 Sep 2026 |
| CIQ-R02 | Mitigate | Implement SHAP explanations; train simpler fallback model | ML Ops | 30 Nov 2026 |
| CIQ-R03 | Mitigate | Weekly PSI monitoring; automatic tempering at 0.2 PSI | ML Ops | 15 Oct 2026 |
| CIQ-R04 | Accept | Rate limiting and encryption implemented | CISO | N/A |
| CIQ-R05 | Mitigate | Complete Annex IV docs; mock regulatory inspection | AI Compliance | 15 Oct 2026 |
| CIQ-R06 | Mitigate | Differential privacy; enhanced audit logging | Privacy Officer | 30 Nov 2026 |
| CIQ-R07 | Mitigate | Cross-train 50 additional underwriters; stress test | Underwriting Manager | 1 Jan 2027 |

---

## 5. Performance Metrics

### 5.1 Key Performance Indicators

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **AUC-ROC** | 0.82 | > 0.80 | ✅ Passed |
| **Accuracy** | 87.4% | > 85% | ✅ Passed |
| **True Positive Rate (TPR)** | 76.2% | > 75% | ✅ Passed |
| **False Positive Rate (FPR)** | 3.8% | < 4.0% | ✅ Passed |
| **Positive Predictive Value** | 68.5% | > 65% | ✅ Passed |
| **Negative Predictive Value** | 92.1% | > 90% | ✅ Passed |

### 5.2 Bias Assessment

| Protected Attribute | DIR | Threshold | Status |
|---------------------|-----|-----------|--------|
| **Race (White vs. Black)** | 74% → 86% (after mitigation) | > 80% | ✅ Passed |
| **Ethnicity (Non-Hispanic vs. Hispanic)** | 80% | > 80% | ✅ Passed |
| **Gender (Male vs. Female)** | 89% | > 80% | ✅ Passed |
| **Age (Prime vs. Young)** | 86% | > 80% | ✅ Passed |
| **Intersectional (White Male vs. Black Female)** | 68% → 82% (after mitigation) | > 80% | ✅ Passed |

### 5.3 Robustness Testing

| Test | Method | Result | Status |
|------|--------|--------|--------|
| **Data Drift (PSI)** | Population Stability Index | 0.12 (Monthly) | 🟡 Warning |
| **Concept Drift** | Performance decay over time | 2% per year | ✅ Passed |
| **Adversarial Robustness** | Evasion attack simulation | 12% success rate | ✅ Passed |
| **Economic Stress Test** | 20% DTI shift | PSI = 0.18 | 🔴 Failed — kill-switch activated at 0.2 |

---

## 6. Human Oversight

### 6.1 Oversight Model

| Attribute | Detail |
|-----------|--------|
| **Oversight Type** | Human-in-the-loop (for borderline scores 580-720) |
| **Coverage** | ~15% of all applications (~360,000 annually) |
| **Oversight Capabilities** | Underwriters receive risk heatmap, model probability score, and three primary drivers (SHAP) |
| **Override Rights** | Underwriters can Approve, Reject, or Refer to Senior Underwriter |
| **Mandatory Justification** | All overrides require written justification (minimum 50 characters) |
| **Logging** | All overrides logged with timestamp, user ID, and justification; retained 7 years |
| **Spot Checks** | Compliance team randomly reviews 5% of overrides monthly |

### 6.2 Escalation Paths

| Scenario | Escalation Path | Approver |
|----------|-----------------|----------|
| **Model Output > 720** | Auto-Approval (no human review) | N/A |
| **Model Output < 580** | Auto-Rejection (no human review) | N/A |
| **Model Output 580-720** | Standard Human Review | Underwriter |
| **Override Decision** | Reviewed by Senior Underwriter | Senior Underwriter |
| **Systemic Override Pattern** | Escalated to AI Governance Council | AI Governance Council |
| **Model Alert (PSI > 0.15)** | Escalated to ML Ops + Model Risk | Head of Model Risk |

---

## 7. Cybersecurity

### 7.1 Security Controls

| Control | Implementation | Status |
|---------|----------------|--------|
| **Data Encryption** | TLS 1.3 at rest and in transit | ✅ Implemented |
| **Access Control** | RBAC + MFA for all admin access | ✅ Implemented |
| **API Rate Limiting** | 1000 requests/minute per IP | ✅ Implemented |
| **Vulnerability Scanning** | Weekly automated scans | ✅ Implemented |
| **Penetration Testing** | Annual third-party pentest | ✅ Implemented |
| **SIEM Integration** | Full logging and alerting | ✅ Implemented |

### 7.2 Adversarial Testing

| Test | Method | Result | Status |
|------|--------|--------|--------|
| **Model Extraction** | API query probing | 3% of features recoverable | ✅ Low Risk |
| **Data Poisoning** | Label flipping (5%) | 8% accuracy drop | ✅ Acceptable |
| **Adversarial Inputs** | Gradient-based evasion | 12% success rate | ✅ Acceptable |

---

## 8. Post-Market Monitoring

### 8.1 Monitoring Plan

| Activity | Frequency | Owner |
|----------|-----------|-------|
| **Performance Monitoring** | Real-time (every 5 min) | ML Ops |
| **Drift Detection** | Daily | ML Ops |
| **Fairness Monitoring** | Weekly | Model Risk |
| **User Complaints Review** | Monthly | Customer Support |
| **Full System Review** | Quarterly | System Owner |
| **Post-Market Monitoring Report** | Monthly | AI Compliance |

### 8.2 Incident Reporting

| Severity | Reporting Timeline | Contact |
|----------|-------------------|---------|
| **Critical** | 2-10 days to authority | CAIO + CISO + AI Governance Council |
| **High** | 15 days to authority | CAIO + Model Risk |
| **Medium** | Internal within 24 hours | System Owner |
| **Low** | Internal within 7 days | System Owner |

---

## 9. Conformity Assessment

### 9.1 Assessment Route

| Assessment Route | Applicability | Status |
|------------------|---------------|--------|
| Internal Assessment | ✅ Yes (not an Annex I system) | In Progress |
| Third-Party Assessment | ❌ No | N/A |

### 9.2 EU Database Registration

| Requirement | Status | Registration Number |
|-------------|--------|---------------------|
| EU Database Registration | 🔴 Pending | TBD |

---

## 10. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | Head of Model Risk | | |
| | AI Compliance Officer | | |
| | CAIO | | |
| | AI Governance Council Chair | | |

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 15 August 2026 | AI Compliance | Initial version — ready for regulatory review |
