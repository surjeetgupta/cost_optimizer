import os
import json
from src.profile_extractor import extract_project_profile
from src.billing_generator import generate_billing
from src.report_builder import build_report

def start_cli():
    while True:
        print("\n1. Generate project profile (TXT → JSON)")
        print("2. Run complete cost analysis")
        print("3. View recommendations")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            extract_project_profile()

        elif choice == "2":
            
            if not os.path.exists("data/project_profile.json"):
                print(" project_profile.json not found. Running extractor first...")
                extract_project_profile()

            generate_billing()
            build_report()

        elif choice == "3":
            with open("data/cost_optimization_report.json") as f:
                report = json.load(f)
            print(json.dumps(report["recommendations"], indent=2))

        elif choice == "4":
            break
