import json
from src.llm_client import call_llm

def generate_billing():
    with open("data/project_profile.json", "r") as fi:
        profile = json.load(fi)

    prompt = f"""
Generate realistic cloud billing data.

RULES:
- Output ONLY JSON array
- 12-20 records
- Budget: {profile['budget_inr_per_month']} INR
- Include compute, database, storage, networking, monitoring

Fields per record:
month, service, resource_id, region,
usage_quantity, unit, cost_inr, desc
"""

    billing = call_llm(prompt)

    with open("data/mock_billing.json", "w") as f:
        json.dump(billing, f, indent=2)

    print("mock_billing.json generated")
