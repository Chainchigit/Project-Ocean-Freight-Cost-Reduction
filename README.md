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

🧱 Data & Features

Core features used in the current version of the model include:

Port – origin/destination port grouping

Year, Month – time dimension for seasonality

Freight Cost Max – historical benchmark / ceiling cost

Other engineered features from the data pipeline (e.g. aggregated statistics)

The project is designed so that additional external variables (e.g. market indices, macro indicators) can be added later to improve accuracy.

🤖 Model

The main model is XGBoost Regressor (XGBRegressor) with parameters such as:

n_estimators = 500

learning_rate = 0.05

max_depth = 6

subsample = 0.8

colsample_bytree = 0.8

objective = "reg:squarederror"

The model is trained on the prepared dataset from the Data pipe line folder and evaluated on a held-out test set.

📈 Current Performance (Test Set)

Key metrics from the latest experiment:

MAE ≈ 336

RMSE ≈ 692

MAPE ≈ 25.6%

MPE ≈ +11.4% (model tends to over-predict slightly)

R² ≈ 0.915

Interpretation:

The model explains ~91% of the variance in freight cost.

Average relative error is around 25%, which is reasonable for a highly volatile cost like ocean freight, but there is still room for improvement (target: MAPE < 20%).

Error analysis by Port / Month is used to identify lanes where the model performs poorly and may require separate treatment or additional features.

🚀 How to Run

You can run this project either in Google Colab or locally.

1. Clone the repository
git clone https://github.com/Chainchigit/Project-Ocean-Freight-Cost-Reduction.git
cd Project-Ocean-Freight-Cost-Reduction

2. Create environment & install dependencies (local)
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt   # (if/when added)


Or, in Google Colab, simply upload the script/notebook and install required libraries:

!pip install xgboost pandas numpy scikit-learn

3. Run the data pipeline

Open the notebooks / scripts under:

Data pipe line/


Typical steps:

Load raw dataset (Excel/CSV).

Clean & transform data.

Export or create a model-ready dataframe.

4. Train the model

Open notebooks / scripts under:

Model Training/


Run the cells to:

Split data into train / test.

Train XGBRegressor.

Generate predictions and performance summary.

(Optional) Export result tables to Excel for business review.

📌 Roadmap / Next Steps

Planned enhancements:

Add external market indices (e.g. global freight indices) as additional features.

Train separate models by region / port cluster to reduce local error.

Implement simple API or dashboard for “what-if” freight scenarios.

Add requirements.txt and more automated scripts (no-click pipeline).

🙋‍♂️ Author

Chainarong Chiewngan (Chainchigit)
Data / DX / Analytics practitioner with interest in logistics, cost optimization, and forecasting.
