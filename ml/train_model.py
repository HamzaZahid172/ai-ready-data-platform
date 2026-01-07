import json
import pickle
from sklearn.linear_model import LogisticRegression

with open("data/features.json") as f:
    data = json.load(f)

X = [[d["total_orders"], d["avg_order_value"]] for d in data]
y = [1 if d["avg_order_value"] > 60 else 0 for d in data]

model = LogisticRegression()
model.fit(X, y)

with open("ml/model.pkl", "wb") as f:
    pickle.dump(model, f)

