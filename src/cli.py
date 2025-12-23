import os
import json
from src.profile_extractor import extract_project_profile

def start_cli():
    while True:
        print("\n1. Generate project profile (TXT → JSON)")
        
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            extract_project_profile()

        elif choice == "2":
            break
