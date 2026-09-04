#!/usr/bin/env python3
"""
EU AI Act Annex IV Validation Script

This script validates that a complete Annex IV documentation package
contains all required sections and content.
"""

import os
import sys
import argparse
import re
from pathlib import Path

# Required sections and their minimum word count thresholds
REQUIRED_SECTIONS = {
    "01-system-description.md": 100,
    "02-data-governance.md": 100,
    "03-technical-architecture.md": 100,
    "04-risk-management.md": 150,
    "05-performance-metrics.md": 100,
    "06-human-oversight.md": 100,
    "07-cybersecurity.md": 100,
    "08-post-market-monitoring.md": 100,
    "09-conformity-assessment.md": 50,
}

# Article mapping for user guidance
ARTICLE_MAPPING = {
    "01-system-description.md": "Arts. 11, 13",
    "02-data-governance.md": "Art. 10",
    "03-technical-architecture.md": "Art. 11",
    "04-risk-management.md": "Art. 9",
    "05-performance-metrics.md": "Art. 15",
    "06-human-oversight.md": "Arts. 13, 14",
    "07-cybersecurity.md": "Art. 15",
    "08-post-market-monitoring.md": "Art. 12, 73",
    "09-conformity-assessment.md": "Arts. 16, 17",
}

def count_words(text):
    """Count words in markdown text (excluding markdown syntax)."""
    # Remove markdown links, headers, tables, etc.
    clean = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove links
    clean = re.sub(r'#{1,6}\s+', '', clean)       # Remove headers
    clean = re.sub(r'\|.*?\|', '', clean)         # Remove table rows
    clean = re.sub(r'```.*?```', '', clean, flags=re.DOTALL)  # Remove code blocks
    clean = re.sub(r'[^\w\s]', ' ', clean)        # Remove punctuation
    words = clean.split()
    return len(words)

def validate_annex_iv(directory):
    """Validate that all required sections exist and have content."""
    
    results = {
        "total": len(REQUIRED_SECTIONS),
        "present": 0,
        "missing": [],
        "below_threshold": [],
        "word_counts": {}
    }
    
    path = Path(directory)
    
    if not path.exists():
        print(f"❌ Error: Directory '{directory}' does not exist")
        return False
    
    print(f"📊 Validating Annex IV documentation in: {directory}")
    print("=" * 60)
    
    for filename, min_words in REQUIRED_SECTIONS.items():
        filepath = path / filename
        article_ref = ARTICLE_MAPPING.get(filename, "N/A")
        
        if not filepath.exists():
            results["missing"].append(filename)
            print(f"❌ MISSING: {filename} (required for {article_ref})")
            continue
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        word_count = count_words(content)
        results["word_counts"][filename] = word_count
        
        if word_count < min_words:
            results["below_threshold"].append({
                "file": filename,
                "words": word_count,
                "threshold": min_words,
                "article": article_ref
            })
            print(f"⚠️  WARNING: {filename} has {word_count} words (need {min_words}+) for {article_ref}")
        else:
            results["present"] += 1
            print(f"✅ PASSED: {filename} ({word_count} words) for {article_ref}")
    
    # Generate summary report
    print("\n" + "=" * 60)
    print("📋 Validation Summary")
    print("=" * 60)
    print(f"✅ Present: {results['present']}/{results['total']}")
    print(f"❌ Missing: {len(results['missing'])}")
    print(f"⚠️  Below Threshold: {len(results['below_threshold'])}")
    
    if results["missing"]:
        print("\n🔴 Missing Files:")
        for f in results["missing"]:
            print(f"   - {f}")
    
    if results["below_threshold"]:
        print("\n🟡 Files Below Word Count Threshold:")
        for item in results["below_threshold"]:
            print(f"   - {item['file']}: {item['words']} words (needs {item['threshold']}) for {item['article']}")
    
    print("\n📊 Article Coverage:")
    for filename, article_ref in ARTICLE_MAPPING.items():
        if filename in results["missing"]:
            status = "❌ MISSING"
        elif filename in [item["file"] for item in results["below_threshold"]]:
            status = "⚠️  INCOMPLETE"
        else:
            status = "✅ COMPLETE"
        print(f"   - {article_ref}: {status}")
    
    # Determine overall status
    if results["missing"]:
        overall = "❌ FAIL — Missing required sections"
    elif results["below_threshold"]:
        overall = "🟡 PARTIAL — Content gaps identified"
    else:
        overall = "✅ PASS — All sections complete"
    
    print("\n" + "=" * 60)
    print(f"🏆 Overall Status: {overall}")
    print("=" * 60)
    
    return len(results["missing"]) == 0 and len(results["below_threshold"]) == 0

def main():
    parser = argparse.ArgumentParser(
        description='Validate EU AI Act Annex IV documentation completeness'
    )
    parser.add_argument('directory', help='Directory containing Annex IV sections')
    parser.add_argument('--strict', action='store_true',
                        help='Treat warnings as failures')
    
    args = parser.parse_args()
    
    success = validate_annex_iv(args.directory)
    sys.exit(0 if success else 1 if not args.strict else 0)

if __name__ == '__main__':
    main()
