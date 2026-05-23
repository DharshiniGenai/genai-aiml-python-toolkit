import csv
from statistics import median

def safe_int(x):

    try:
        return int(str(x).strip())
    except:
        return None

def safe_float(x):

    try:
        return float(str(x).strip())
    except:
        return None

def clean_data(rows):

    latest = {}

    valid_ages = []
    valid_income = []

    # ---------------------------------
    # FIRST PASS
    # Collect valid values
    # ---------------------------------

    for r in rows:

        age = safe_int(r["age"])
        income = safe_float(r["income"])

        if age is not None and 0 <= age <= 100:
            valid_ages.append(age)

        if income is not None and income < 1000000:
            valid_income.append(income)

    median_age = int(median(valid_ages))
    median_income = median(valid_income)

    cleaned = []

    # ---------------------------------
    # SECOND PASS
    # Cleaning
    # ---------------------------------

    for r in rows:

        # Standardize missing values
        for k in r:

            if str(r[k]).strip() in [
                "",
                "null",
                "None",
                "N/A",
                "n/a"
            ]:
                r[k] = None

        # -------------------------
        # AGE CLEANING
        # -------------------------

        age = safe_int(r["age"])

        if age is None or age < 0 or age > 100:
            age = median_age

        r["age"] = age

        # -------------------------
        # INCOME CLEANING
        # -------------------------

        income = safe_float(r["income"])

        if income is None or income > 1000000:
            income = median_income

        r["income"] = income

        # -------------------------
        # CITY CLEANING
        # -------------------------

        if not r["city"]:
            r["city"] = "Unknown"

        else:
            r["city"] = r["city"].strip()

        # -------------------------
        # PURCHASED CLEANING
        # -------------------------

        val = str(r["purchased"]).strip().lower()

        if val in ["true", "yes", "1"]:
            r["purchased"] = True

        else:
            r["purchased"] = False

        # -------------------------
        # FEATURE ENGINEERING
        # -------------------------

        r["is_adult"] = r["age"] >= 18

        if r["income"] < 30000:
            r["income_bucket"] = "Low"

        elif r["income"] < 70000:
            r["income_bucket"] = "Mid"

        else:
            r["income_bucket"] = "High"

        # -------------------------
        # REMOVE DUPLICATES
        # Keep latest signup_date
        # -------------------------

        uid = r["user_id"]

        if uid not in latest:

            latest[uid] = r

        else:

            if r["signup_date"] > latest[uid]["signup_date"]:
                latest[uid] = r

    cleaned = list(latest.values())

    return cleaned

def save_clean_data(data):

    with open("outputs/clean_data.csv", "w", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )

        writer.writeheader()

        writer.writerows(data)