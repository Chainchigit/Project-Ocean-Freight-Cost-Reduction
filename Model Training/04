# ---------------------------
# แยก X / y + ทำ One-hot
# ---------------------------

X_raw = df_model[available_features]
y = df_model[TARGET_COL].astype(float)

# แปลง category (object) → one-hot
X = pd.get_dummies(X_raw, drop_first=True)

print("Shape X:", X.shape)
print("Shape y:", y.shape)
