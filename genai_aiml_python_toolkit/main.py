import os

from loader import load_data
from cleaner import clean_data, save_clean_data
from features import build_feature_store
from predictor import run_classifier
from text_analytics import analyze_feedback
from report import generate_summary

# Create folders automatically
os.makedirs("outputs", exist_ok=True)
os.makedirs("input", exist_ok=True)

def run_pipeline():

    print("\nLOADING DATA...")

    rows = load_data("input/raw_data.csv")

    print("CLEANING DATA...")

    cleaned = clean_data(rows)

    save_clean_data(cleaned)

    generate_summary(cleaned)

    print("BUILDING FEATURE STORE...")

    build_feature_store(cleaned)

    print("RUNNING CLASSIFIER...")

    run_classifier(cleaned)

    print("RUNNING TEXT ANALYTICS...")

    analyze_feedback()

    print("\nALL FILES GENERATED SUCCESSFULLY")

while True:

    print("\n===== AI/ML TOOLKIT =====")
    print("1. Run Full Pipeline")
    print("2. Exit")

    ch = input("Enter choice: ")

    if ch == "1":

        run_pipeline()

    elif ch == "2":

        break

    else:

        print("Invalid Choice")