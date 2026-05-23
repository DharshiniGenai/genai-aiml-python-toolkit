import csv
import json

def load_data(file_path):

    if file_path.endswith(".csv"):

        with open(file_path, "r") as f:

            return list(csv.DictReader(f))

    elif file_path.endswith(".json"):

        with open(file_path, "r") as f:

            return json.load(f)

    else:

        raise ValueError("Unsupported file format")