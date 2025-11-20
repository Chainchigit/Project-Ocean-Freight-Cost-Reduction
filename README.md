# 🚢 Project Ocean Freight Cost Reduction 

This project focuses on leveraging **data analytics and machine learning (XGBoost)** to reduce ocean freight costs through accurate forecasting and insight generation.

> Better forecasting → Better contract negotiation → Better cost efficiency

---

## 🎯 Project Goals

- Analyze freight cost behavior across **Ports / Year / Month**
- Build a predictive model to forecast freight rates
- Evaluate performance with real business metrics
- Provide a scalable data pipeline for future enhancements

---

## 📂 Repository Overview

```text
Project-Ocean-Freight-Cost-Reduction/
│
├── Data pipe line/   
│   ├─ Data cleaning
│   └─ Feature engineering
│
├── Model Training/
│   ├─ XGBoost training
│   └─ Performance evaluation
│
└── README.md
```

## 🧱 Data & Features

Key features used in the current model:

Feature	Description
Port	Port group for shipping lanes
Year / Month	Time dimension for seasonal effects
Freight Cost Max	Historical ceiling benchmark
Engineered Features	Aggregated or transformed values for modeling

The project is built to allow additional external data (e.g., freight indices, macro economics) to be included in future versions.

---

## 🤖 Model

Main model: XGBoost Regressor

Parameters used:

n_estimators = 500

learning_rate = 0.05

max_depth = 6

subsample = 0.8

colsample_bytree = 0.8

objective = "reg:squarederror"

Evaluation: Train-test split with performance metrics reported below.

## 📈 Model Performance (Test Set)

Metric	Value	Interpretation

MAE	~336	    Average error in USD per container

RMSE	~692	  Indicates some large-error cases

MAPE	~25.6%	Reasonable for volatile cost data

MPE	+11.4%	  Slight over-prediction bias

R²	0.915   	Model explains ~91% of variance ⭐

---
## Backtest

![Uploading image.png…]()


## Summary

Model captures the pattern very well

Some lanes still show high variability → optimization potential

Next step goal: MAPE < 20%

---

## 🙋‍♂️ Author

Chainarong C. (Chainchigit)
Data / DX / Analytics practitioner
