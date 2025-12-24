import json
from src.cost_analyzer import analyze_costs
from src.recommender import generate_recommendations

def build_report():
    analysis = analyze_costs()
    recommendations = generate_recommendations(analysis)

    report = {
        "analysis": analysis,
        "recommendations": recommendations
    }

    with open("data/cost_optimization_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("cost_optimization_report.json generated")
