import json
from collections import defaultdict, Counter

def build_feature_store(users):

    store = defaultdict(lambda: {
        "total_events": 0,
        "views_count": 0,
        "cart_count": 0,
        "purchase_count": 0,
        "prices": [],
        "products": []
    })

    for u in users:

        uid = u["user_id"]

        store[uid]["total_events"] += 1
        store[uid]["views_count"] += 2

        if u["income_bucket"] != "Low":
            store[uid]["cart_count"] += 1

        if u["income_bucket"] == "High":
            store[uid]["purchase_count"] += 1

        store[uid]["prices"].append(u["income"])
        store[uid]["products"].append("ProductA")

    final = {}

    for uid, v in store.items():

        final[uid] = {

            "total_events": v["total_events"],

            "views_count": v["views_count"],

            "cart_count": v["cart_count"],

            "purchase_count": v["purchase_count"],

            "avg_price_viewed":
                sum(v["prices"]) / len(v["prices"]),

            "most_viewed_product":
                Counter(v["products"]).most_common(1)[0][0],

            "conversion_flag":
                int(v["purchase_count"] > 0)
        }

    with open("outputs/feature_store.json", "w") as f:
        json.dump(final, f, indent=4)

    return final