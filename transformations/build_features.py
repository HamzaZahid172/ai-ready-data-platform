import json
from collections import defaultdict

def build(input_file, output_file):
    stats = defaultdict(list)

    with open(input_file) as f:
        events = json.load(f)

    for e in events:
        stats[e["user_id"]].append(e["order_value"])

    features = []
    for user, values in stats.items():
        features.append({
            "user_id": user,
            "total_orders": len(values),
            "avg_order_value": sum(values) / len(values)
        })

    with open(output_file, "w") as f:
        json.dump(features, f, indent=2)

if __name__ == "__main__":
    build("data/validated.json", "data/features.json")
