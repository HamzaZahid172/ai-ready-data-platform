const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/predict", (req, res) => {
  const { total_orders, avg_order_value } = req.body;

  if (
    typeof total_orders !== "number" ||
    typeof avg_order_value !== "number"
  ) {
    return res.status(400).json({ error: "Invalid input" });
  }

  const prediction = avg_order_value > 60 ? "high_value" : "low_value";
  res.json({ prediction });
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`API running on port ${PORT}`);
});
