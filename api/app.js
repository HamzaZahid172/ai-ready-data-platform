const express = require("express");
const app = express();

app.use(express.json());

app.post("/predict", (req, res) => {
  const { total_orders, avg_order_value } = req.body;
  const prediction = avg_order_value > 60 ? "high_value" : "low_value";
  res.json({ prediction });
});

app.listen(3000, () => console.log("API running on port 3000"));
