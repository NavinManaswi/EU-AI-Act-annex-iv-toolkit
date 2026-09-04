#!/usr/bin/env python3
"""
EU AI Act Annex IV Documentation Generator

This script scaffolds a complete Annex IV documentation package
for a new AI system.
"""

import os
import sys
import argparse
from datetime import datetime

def create_template(system_name, output_dir):
    """Create the full Annex IV template structure."""
    
    sections = {
        "01-system-description.md": """# 1. System Description

## 1.1 General Description

| Attribute | Detail |
|-----------|--------|
| **System Name** | {system_name} |
| **System Type** | [Predictive/Generative/Agentic] |
| **Model Architecture** | [Model type] |
| **Intended Purpose** | [Description] |
| **Decision Authority** | [Fully automated/Human-in-the-loop] |
| **Deployment Jurisdictions** | [EU, UK, US, etc.] |
| **Affected Population** | [Number and description] |

## 1.2 Intended Use

[Describe the intended purpose, target users, and deployment context.]

## 1.3 System Boundaries

[Describe what the system does and does not do.]
""",

        "02-data-governance.md": """# 2. Data Governance

## 2.1 Training Data Overview

| Attribute | Detail |
|-----------|--------|
| **Source** | [Description] |
| **Volume** | [Number of records] |
| **Features** | [Number and types] |
| **Protected Attributes** | [Excluded/included] |
| **Proxy Risk Identified** | [Yes/No — details] |

## 2.2 Data Quality Controls

| Control | Implementation | Owner |
|---------|----------------|-------|
| [Control 1] | [Implementation] | [Owner] |

## 2.3 Data Privacy

[Describe privacy controls, GDPR/CCPA compliance, and data retention policies.]
""",

        "03-technical-architecture.md": """# 3. Technical Architecture

## 3.1 Architecture Overview

[Describe the system architecture, including components, data flow, and dependencies.]

## 3.2 Data Flow Diagram
[Source Systems]
↓
[Data Processing Pipeline]
↓
[Model Inference]
↓
[Decision Output]
↓
[Explanation Layer]

  
## 3.3 Infrastructure

[Describe deployment environment, cloud infrastructure, and scaling requirements.]
""",

        "04-risk-management.md": """# 4. Risk Management

## 4.1 Risk Identification

| Risk ID | Description | Category | Inherent Risk |
|---------|-------------|----------|---------------|
| [ID]-01 | [Description] | [Category] | [Level] |

## 4.2 Risk Analysis

| Risk ID | Likelihood | Impact | Control | Residual Risk |
|---------|------------|--------|---------|---------------|
| [ID]-01 | [Level] | [Level] | [Description] | [Level] |

## 4.3 Risk Treatment

| Risk ID | Treatment Decision | Treatment Plan | Owner | Target Date |
|---------|-------------------|----------------|-------|-------------|
| [ID]-01 | [Mitigate/Accept/Transfer] | [Description] | [Owner] | [Date] |
""",

        "05-performance-metrics.md": """# 5. Performance Metrics

## 5.1 Key Performance Indicators

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| [Metric 1] | [Value] | [Target] | [Pass/Fail] |

## 5.2 Bias Assessment

| Protected Attribute | DIR | Threshold | Status |
|---------------------|-----|-----------|--------|
| [Attribute] | [Value] | > 80% | [Pass/Fail] |

## 5.3 Robustness Testing

| Test | Method | Result | Status |
|------|--------|--------|--------|
| [Test] | [Method] | [Result] | [Pass/Fail] |
""",

        "06-human-oversight.md": """# 6. Human Oversight

## 6.1 Oversight Model

| Attribute | Detail |
|-----------|--------|
| **Oversight Type** | [Human-in-the-loop/Human-on-the-loop] |
| **Coverage** | [Percentage/Description] |
| **Oversight Capabilities** | [What tools and information are provided] |
| **Override Rights** | [What can be overridden] |

## 6.2 Escalation Paths

| Scenario | Escalation Path | Approver |
|----------|-----------------|----------|
| [Scenario] | [Path] | [Approver] |
""",

        "07-cybersecurity.md": """# 7. Cybersecurity

## 7.1 Security Controls

| Control | Implementation | Status |
|---------|----------------|--------|
| [Control 1] | [Implementation] | [Status] |

## 7.2 Adversarial Testing

| Test | Method | Result | Status |
|------|--------|--------|--------|
| [Test] | [Method] | [Result] | [Status] |
""",

        "08-post-market-monitoring.md": """# 8. Post-Market Monitoring

## 8.1 Monitoring Plan

| Activity | Frequency | Owner |
|----------|-----------|-------|
| [Activity 1] | [Frequency] | [Owner] |

## 8.2 Incident Reporting

| Severity | Reporting Timeline | Contact |
|----------|-------------------|---------|
| Critical | 2-10 days | [Contact] |
| High | 15 days | [Contact] |
""",

        "09-conformity-assessment.md": """# 9. Conformity Assessment

## 9.1 Assessment Route

| Assessment Route | Applicability | Status |
|------------------|---------------|--------|
| Internal Assessment | [Yes/No] | [Status] |
| Third-Party Assessment | [Yes/No] | [Status] |

## 9.2 EU Database Registration

| Requirement | Status | Registration Number |
|-------------|--------|---------------------|
| EU Database Registration | [Pending/Complete] | [Number] |
"""
    }

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Write each section
    for filename, content in sections.items():
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content.format(system_name=system_name))
        print(f"✅ Created: {filepath}")

    print(f"\n🎯 Annex IV documentation package scaffolded for '{system_name}'")
    print(f"📁 Location: {output_dir}/")
    print(f"\nNext steps:")
    print("1. Review each section and fill in the placeholders")
    print("2. Reference the CreditIQ example for guidance")
    print("3. Run the validation script to check completeness")

def main():
    parser = argparse.ArgumentParser(
        description='Scaffold EU AI Act Annex IV documentation'
    )
    parser.add_argument('system_name', help='Name of the AI system')
    parser.add_argument('--output', '-o', default='annex-iv-output',
                        help='Output directory (default: annex-iv-output)')
    parser.add_argument('--date', default=datetime.now().strftime('%Y-%m-%d'),
                        help='Document date (default: today)')
    
    args = parser.parse_args()
    
    print(f"🚀 Generating Annex IV documentation for: {args.system_name}")
    print(f"📅 Date: {args.date}")
    print(f"📁 Output: {args.output}/")
    print()
    
    create_template(args.system_name, args.output)

if __name__ == '__main__':
    main()
