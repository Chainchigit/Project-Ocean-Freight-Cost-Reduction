# ---------------------------
# ตั้งค่าคอลัมน์เป้า + candidate features
# ---------------------------

TARGET_COL = "Freight (USD/Con')"   # คอลัมน์ที่อยากทำนาย

# ใช้แค่คอลัมน์ด้านล่างเป็น feature (ไม่มี Mode, ไม่มี TARGET)
CANDIDATE_FEATURES = [
    "Port",
    "Month",
    "Year",
    "Freight Cost Max",
    #"Freight (USD/Con')",
]

# เอา space ออกเผื่อชื่อคอลัมน์มีช่องว่าง
df.columns = df.columns.str.strip()

# เลือกเฉพาะ feature ที่มีจริงใน df
available_features = [c for c in CANDIDATE_FEATURES if c in df.columns]
missing_features   = [c for c in CANDIDATE_FEATURES if c not in df.columns]

print("ใช้ feature เหล่านี้:", available_features)
if missing_features:
    print("คอลัมน์ต่อไปนี้ไม่มีใน df และจะไม่ถูกใช้:", missing_features)

# สร้าง df_model จาก feature + target
cols_for_model = available_features + [TARGET_COL]
df_model = df[cols_for_model].copy()

# แปลง target เป็นตัวเลข
df_model[TARGET_COL] = pd.to_numeric(df_model[TARGET_COL], errors="coerce")

# ลบแถวที่ target เป็น NaN
df_model = df_model.dropna(subset=[TARGET_COL])

print("จำนวนแถวหลังจัดการ target:", df_model.shape[0])
