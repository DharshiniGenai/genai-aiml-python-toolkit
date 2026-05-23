import csv

def run_classifier(users):

    preds = []
    actual = []

    for u in users:

        score = 0
        rules = []

        if u["income_bucket"] == "High":
            score += 2
            rules.append("high_income")

        if u["is_adult"]:
            score += 1
            rules.append("adult")

        pred = 1 if score >= 2 else 0

        true = 1 if u["income_bucket"] == "High" else 0

        preds.append(pred)
        actual.append(true)

        u["prediction"] = pred
        u["score"] = score
        u["rules"] = "|".join(rules)

    accuracy = sum(
        p == a for p, a in zip(preds, actual)
    ) / len(actual)

    with open("outputs/predictions.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "user_id",
            "prediction",
            "score",
            "rules"
        ])

        for u in users:

            writer.writerow([
                u["user_id"],
                u["prediction"],
                u["score"],
                u["rules"]
            ])

    with open("outputs/evaluation.txt", "w") as f:

        f.write(f"Accuracy: {accuracy:.2f}\n")