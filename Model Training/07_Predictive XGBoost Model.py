import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------------------------
# 1) Predict ด้วย XGBoost
# ---------------------------
y_pred = xgb_model.predict(X_test)   # <-- ใช้ xgb_model ให้ตรงกับที่เทรน

# ---------------------------
# 2) สร้างตาราง result_preview
# ---------------------------
raw_test = X_raw.loc[X_test.index].copy()

result_preview = pd.DataFrame({
    "Port": raw_test["Port"],
    "Year": raw_test["Year"],
    "Month": raw_test["Month"],
    "Freight Cost Max": raw_test.get("Freight Cost Max"),
    "Actual": y_test.values,
    "Predicted": y_pred
})

# วัดผลรายแถว
result_preview["Error"] = result_preview["Predicted"] - result_preview["Actual"]
result_preview["Abs_Error"] = result_preview["Error"].abs()
result_preview["APE_%"] = (
    result_preview["Abs_Error"] / result_preview["Actual"].replace(0, np.nan)
) * 100

print("=== ตัวอย่าง 10 แถวที่ Error มากสุด ===")
print(result_preview.sort_values("Abs_Error", ascending=False).head(5))

# ---------------------------
# 3) Overall performance
# ---------------------------
y_true = result_preview["Actual"].values

mae  = mean_absolute_error(y_true, y_pred)
mse  = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_true, y_pred)

mape = result_preview["APE_%"].mean()
mpe  = (
    (result_preview["Error"] /
     result_preview["Actual"].replace(0, np.nan) * 100)
).mean()

perf_summary = pd.DataFrame({
    "Metric": ["MAE", "RMSE", "MAPE_%", "MPE_%", "R2"],
    "Value":  [mae,  rmse,  mape,     mpe,     r2]
})

print("\n=== Overall Performance ===")
print(perf_summary)

# ---------------------------
# 4) Performance by Port
# ---------------------------
perf_by_port = (
    result_preview
    .groupby("Port")
    .agg(**{
        "N": ("Actual", "size"),
        "MAE": ("Abs_Error", "mean"),
        "MAPE_%": ("APE_%", "mean")
    })
    .reset_index()
    .sort_values("MAE", ascending=True)
)

print("\n=== Performance by Port (Top 10) ===")
print(perf_by_port.head(5))
