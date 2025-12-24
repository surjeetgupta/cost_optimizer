import json
from collections import defaultdict

def analyze_costs():
    with open("data/project_profile.json") as f:
        profile = json.load(f)

    with open("data/mock_billing.json") as f:
        billing = json.load(f)

    total_cost = 0
    service_costs = defaultdict(int)

    for item in billing:
        total_cost += item["cost_inr"]
        service_costs[item["service"]] += item["cost_inr"]

    budget = profile["budget_inr_per_month"]

    return {
        "total_monthly_cost": total_cost,
        "budget": budget,
        "budget_variance": total_cost - budget,
        "service_costs": dict(service_costs),
        "is_over_budget": total_cost > budget
    }
