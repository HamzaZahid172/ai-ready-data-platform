import json

REQUIRED = ["user_id", "order_value", "timestamp"]

def validate(input_file, output_file):
    with open(input_file) as f:
        payload = json.load(f)

    valid = []
    for e in payload["events"]:
        if all(k in e for k in REQUIRED):
            valid.append(e)

    with open(output_file, "w") as f:
        json.dump(valid, f, indent=2)

if __name__ == "__main__":
    validate("data/ingested.json", "data/validated.json")

