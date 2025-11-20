# ถ้ายังไม่มี pandas / openpyxl ให้รันบรรทัดนี้ก่อน (รันครั้งเดียวพอ)
!pip install pandas openpyxl --quiet

import pandas as pd
from io import BytesIO
from google.colab import files

# 1) อัปโหลดไฟล์ (เลือกได้หลายไฟล์)
print("เลือกไฟล์ Excel ที่ต้องการรวม (เลือกได้หลายไฟล์)...")
uploaded = files.upload()

all_dfs = []  # เก็บ DataFrame ของทุกชีทจากทุกไฟล์

# ===================== CONFIG (ปรับได้) =====================
# ถ้าอยากรวมทุกชีททุกไฟล์ ให้ปล่อยสองตัวแปรนี้ว่างไว้
include_sheets = []   # เช่น ["Sheet1", "Sheet2"]  ถ้าต้องการเฉพาะบางชีท
exclude_sheets = []   # เช่น ["Summary", "Pivot"]  ถ้าไม่เอาบางชีท
# ===========================================================

for filename, file_content in uploaded.items():
    print(f"\nกำลังอ่านไฟล์: {filename}")
    xls = pd.ExcelFile(BytesIO(file_content))

    for sheet_name in xls.sheet_names:
        # ถ้ามี include_sheets ให้เอาเฉพาะชื่อที่ระบุ
        if include_sheets and sheet_name not in include_sheets:
            continue

        # ถ้าอยู่ใน exclude_sheets ให้ข้าม
        if sheet_name in exclude_sheets:
            continue

        print(f"  - รวมชีท: {sheet_name}")
        df = xls.parse(sheet_name)

        # เพิ่มคอลัมน์บอกแหล่งที่มา
        df["SourceFile"] = filename
        df["SourceSheet"] = sheet_name

        all_dfs.append(df)

# ถ้าไม่มีข้อมูลเลย
if not all_dfs:
    raise ValueError("ไม่มีข้อมูลจากชีทใดเลย ตรวจชื่อ include_sheets / exclude_sheets อีกครั้ง")

# 2) รวมทุก DataFrame ต่อกันแนวตั้ง
combined_df = pd.concat(all_dfs, ignore_index=True)

print("\nตัวอย่างข้อมูลที่รวมแล้ว (5 แถวแรก):")
display(combined_df.head())

# 3) เซฟเป็นไฟล์ Excel ใหม่
output_name = "combined.xlsx"
combined_df.to_excel(output_name, index=False)
print(f"\nบันทึกไฟล์รวมแล้วเป็น: {output_name}")

# 4) ให้ดาวน์โหลดไฟล์
files.download(output_name)
