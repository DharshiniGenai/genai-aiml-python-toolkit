import csv
from collections import Counter

def analyze_feedback():

    pos = ["great", "excellent", "love", "easy"]
    neg = ["bad", "slow", "hard", "expensive"]

    with open("input/feedback.txt") as f:
        lines = f.readlines()

    results = []

    pos_words = []
    neg_words = []

    for line in lines:

        uid, text = line.strip().split("|")

        words = text.lower().split()

        p = sum(w in pos for w in words)
        n = sum(w in neg for w in words)

        pos_words.extend([w for w in words if w in pos])
        neg_words.extend([w for w in words if w in neg])

        score = p - n

        sentiment = "Positive" if score >= 0 else "Negative"

        results.append([
            uid,
            score,
            sentiment
        ])

    with open("outputs/feedback_scores.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "user_id",
            "score",
            "sentiment"
        ])

        writer.writerows(results)

    with open("outputs/insights_report.txt", "w") as f:

        f.write("Top Positive Words:\n")

        for w, c in Counter(pos_words).most_common(3):
            f.write(f"{w}: {c}\n")

        f.write("\nTop Negative Words:\n")

        for w, c in Counter(neg_words).most_common(3):
            f.write(f"{w}: {c}\n")