import json
from src.llm_client import call_llm

def extract_project_profile():
    with open("data/project_description.txt", "r", encoding="utf-8") as f:
        description = f.read()

    prompt = f"""
Extract structured project details.

RULES:
- Output ONLY valid JSON
- No explanations
- No markdown

Fields:
name
budget_inr_per_month
description
tech_stack
non_functional_requirements

Input:
{description}
"""

    profile = call_llm(prompt)

    with open("data/project_profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)

    print(" project_profile.json generated")
