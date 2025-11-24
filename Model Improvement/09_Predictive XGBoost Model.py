import numpy as np
import pandas as pd

# -----------------------------
# 1) รายชื่อ Port (ตามที่มี)
# -----------------------------
port_list = [
    "SHANGHAI","KOBE","YOKOHAMA","YOKKAICHI","KAOHSIUNG","PORT KLANG",
    "HO CHI MINH CITY","BUSAN","DURBAN","ANTWERP","CEBU","KATTUPALLI L&T KATTU",
    "KATTUPALLI L&T","CHENGDU","CHATTOGRAM","HAKATA","HUANGPU","KEELUNG",
    "RIO HAINA","SANTOS","SURABAYA","TEMA","TAICHUNG","HO CHI MINH","CHICAGO",
    "AUCKLAND","SYDNEY","MANILA NORTH HARBOUR","ABIDJAN","SINGAPORE",
    "MANILA NORTH HA","JAKARTA","LAGOS","PORT AU PRINCE","BRISBANE","CASABLANCA",
    "HONG KONG","KARACHI","PUERTO QUETZAL","MANILA","ALEXANDRIA","DAKAR",
    "HAIPHONG","YANGON","APAPA","ASHDOD","MANZANILLO","MELBOURNE","SHEKOU",
    "ISTANBUL","IZMIR","LAZARO CARDENAS","GEBZE","BANGKOK","PAT BANGKOK",
    "NANSHA","BUENAVENTURA","LAEM CHABANG","THILAWA","MOMBASA","LOS ANGELES",
    "ABU DHABI"
]

# -----------------------------
# 2) สร้าง max ต่อ Port จากข้อมูลจริง
# -----------------------------
if "Freight Cost Max" in available_features:
    port_max = df_model.groupby("Port")["Freight Cost Max"].max()
else:
    port_max = None

# -----------------------------
# 3) สร้างเดือนอนาคต 7 เดือน
#    (เริ่ม Dec.25 - June.26 → 7 periods)
# -----------------------------
future_dates = pd.date_range(start="2025-12-01", periods=7, freq="MS")

# Port x Month
future_df = pd.DataFrame(
    [(p, d.year, d.month) for p in port_list for d in future_dates],
    columns=["Port", "Year", "Month"]
)

# -----------------------------
# 4) base cost + random variance 1–25%
# -----------------------------
if port_max is not None:
    # base = 0.27 * max ของ port นั้น ๆ
    base_cost = 0.27 * future_df["Port"].map(port_max)

    # สร้างตัวสุ่ม reproducible (ถ้าอยากเปลี่ยนก็เปลี่ยน seed ได้)
    rng = np.random.default_rng(seed=42)

    # Setting variance 1–25%
    var_size = rng.uniform(0.01, 0.25, size=len(future_df))

    # Sampling ทิศทาง + หรือ -
    direction = rng.choice([-1, 1], size=len(future_df))

    # คำนวณ % variance (เชิง signed)
    variance_pct = direction * var_size   # เช่น -0.035, +0.089 ฯลฯ

    # เก็บไว้ดูในตาราง (optional)
    future_df["VariancePct"] = variance_pct

    # คำนวณค่า forecast หลังใส่ variance
    future_df["Freight Cost Max Forecast"] = base_cost * (1 + variance_pct)

    # ถ้าอยากเก็บ base เดิมไว้ด้วย
    future_df["Freight Cost Max Base"] = base_cost

future_df
