import json
from src.llm_client import call_llm

def generate_recommendations(analysis):
    prompt = f"""
You are a cloud cost optimization expert.

RULES:
- Output ONLY valid JSON
- 6-10 recommendations
- Include AWS, Azure, GCP, open-source/free-tier options

Analysis:
{json.dumps(analysis)}
"""

    return call_llm(prompt)
