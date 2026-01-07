# AI-Ready Data Platform

An end-to-end, production-style data engineering project that demonstrates how raw event data can be transformed into machine-learning-ready features and served through a backend API with a simple web UI.

This project reflects real-world data engineering and ML workflows, focusing on clean pipelines, clear separation of concerns, and operational readiness.

---

## Overview

In many real systems, raw event data is not directly usable for analytics or machine learning. It must be ingested, validated, transformed into features, and then exposed to downstream systems such as ML models and APIs.

This project demonstrates that full lifecycle by building a simple but realistic AI-ready data platform.

---

## What This Project Does

- Processes raw event data  
- Ensures data quality through validation  
- Generates ML-ready features  
- Trains a simple machine learning model  
- Serves predictions through an API  
- Displays results using a web UI  

---

## High-Level Architecture

```
Raw Event Data
      ↓
Ingestion (Python)
      ↓
Data Validation (Python)
      ↓
Feature Engineering
      ↓
ML Training (Python)
      ↓
Inference API (Node.js + Express)
      ↓
Web UI (HTML + JavaScript)
```

---

## Tech Stack

- Python – data ingestion, validation, feature engineering, ML training  
- Node.js + Express – inference API  
- JavaScript / HTML – simple web UI  
- SQL – analytics and feature query examples  
- GitHub Actions – CI pipeline  
- AWS concepts – data lake, serverless ingestion (design level)  

---

## Project Structure

```
ai-ready-data-platform/
├── data/                     # Sample data and pipeline outputs
├── ingestion/                # Data ingestion logic
├── transformations/          # Validation and feature engineering
│   └── sql/                  # Example analytics queries
├── ml/                       # Model training logic
├── api/                      # Node.js inference API
├── ui/                       # Simple UI for predictions
├── infra/                    # Architecture / infra notes
└── .github/workflows/        # CI/CD pipeline
```

---

## How the Project Works

### 1. Data Ingestion
Raw event data (JSON) is ingested using Python. This simulates an AWS Lambda-style ingestion writing data into a data lake.

### 2. Data Validation
Incoming data is validated to ensure required fields are present. Invalid records are filtered out to maintain data quality.

### 3. Feature Engineering
Validated data is transformed into ML-ready features such as:
- Total orders per user  
- Average order value  

### 4. Machine Learning Training
A simple machine learning model is trained using the generated features and saved as a reusable artifact.

### 5. Inference API
A Node.js + Express API exposes a `/predict` endpoint that accepts feature values and returns a prediction.

### 6. Web UI
A lightweight web UI allows users to input feature values and view predictions in real time.

---

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/HamzaZahid172/ai-ready-data-platform.git
cd ai-ready-data-platform
```

---

### 2. Run the Data Pipeline (Python)

```bash
python3 -m venv venv
source venv/bin/activate
pip install scikit-learn

python ingestion/ingest.py
python transformations/validate_data.py
python transformations/build_features.py
python ml/train_model.py
```

---

### 3. Run the Inference API

```bash
cd api
npm install
node app.js
```

The API will start at:

```
http://localhost:3000
```

---

### 4. Run the UI

Open the following file in your browser:

```
ui/index.html
```

Enter feature values and click **Predict** to see the result.

---

## API Example

**Endpoint**
```
POST /predict
```

**Request**
```json
{
  "total_orders": 5,
  "avg_order_value": 90
}
```

**Response**
```json
{
  "prediction": "high_value"
}
```

---

## CI/CD

This repository includes a GitHub Actions workflow that sets up the Python environment, installs dependencies, and runs the ML training step automatically on each push.

---

## Deployment (Free Options)

- UI: GitHub Pages  
- API: Render, Railway, or Vercel (free tiers)  

---

## Future Improvements

- Dockerize all services  
- Load the trained ML model directly in the API  
- Use real cloud storage such as AWS S3  
- Add monitoring and logging  
- Add model versioning and experiment tracking  

---

## Author

Hamza Zahid Butt
Senior Software Engineer
