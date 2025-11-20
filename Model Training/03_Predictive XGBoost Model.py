# ---------------------------
# ตั้งค่าคอลัมน์เป้าหมาย + candidate features
# ---------------------------

# ชื่อคอลัมน์ target (แก้ให้ตรงชื่อใน df ถ้าไม่ตรง)
TARGET_COL = "Freight Cost Max"      # สิ่งที่อยากทำนาย

# candidate features - ใส่ชื่อที่ "คิดว่า" มีอยู่ใน df
CANDIDATE_FEATURES = [
    "Port",
    "Month",
    "Year",
    "Mode",
    #"Freight (USD/Con')" ,
    "Freight (USD/Con')" ,
]

# เคลียร์ชื่อคอลัมน์กัน space แปลก ๆ
df.columns = df.columns.str.strip()

# เลือกเฉพาะ feature ที่มีอยู่จริงใน df
available_features = [c for c in CANDIDATE_FEATURES if c in df.columns]
missing_features   = [c for c in CANDIDATE_FEATURES if c not in df.columns]

print(" ใช้ feature เหล่านี้:", available_features)
if missing_features:
    print(" คอลัมน์ต่อไปนี้ไม่มีใน df และจะไม่ถูกใช้:", missing_features)

# สร้าง df_model เฉพาะคอลัมน์ที่มีจริง + target
cols_for_model = available_features + [TARGET_COL]
df_model = df[cols_for_model].copy()

# แปลง target เป็นตัวเลข
df_model[TARGET_COL] = pd.to_numeric(df_model[TARGET_COL], errors="coerce")

# ลบแถวที่ target เป็น NaN
df_model = df_model.dropna(subset=[TARGET_COL])

print("จำนวนแถวหลังเคลียร์ target:", df_model.shape[0])
