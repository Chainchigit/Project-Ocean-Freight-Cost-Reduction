# Project – Ocean Freight Cost Reduction

This repository contains an end-to-end analytics and machine learning project that focuses on **reducing ocean freight cost** by understanding historical patterns and forecasting future freight rates.

The project is structured around a simple idea:

> If we can forecast container freight cost with reasonable accuracy and understand the key drivers,  
> we can negotiate better contracts, choose better routes, and plan shipments more intelligently.

---

## 🎯 Objectives

- Analyze historical ocean freight data (by **port, year, month** and cost).
- Build a **regression model** to predict future freight cost.
- Evaluate model performance with business-friendly metrics (MAPE, MAE, RMSE, R²).
- Provide a data pipeline that can be re-used / extended for future experiments.

---

## 📂 Repository Structure

```text
Project-Ocean-Freight-Cost-Reduction/
│
├── Data pipe line/        # Scripts / notebooks for data cleaning & feature engineering
│   ├─ (load, clean, transform raw data)
│   └─ (create model-ready dataset for training)
│
├── Model Training/        # Scripts / notebooks for model training & evaluation
│   ├─ XGBoost training
│   └─ Performance analysis (MAE, RMSE, MAPE, R², by Port, etc.)
│
└── (future) README.md     # Project documentation
