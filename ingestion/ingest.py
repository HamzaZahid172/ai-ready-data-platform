import json
from datetime import datetime

def ingest(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)

    payload = {
        "ingested_at": datetime.utcnow().isoformat(),
        "events": data
    }

    with open(output_file, "w") as f:
        json.dump(payload, f, indent=2)

if __name__ == "__main__":
    ingest("data/raw_events.json", "data/ingested.json")
