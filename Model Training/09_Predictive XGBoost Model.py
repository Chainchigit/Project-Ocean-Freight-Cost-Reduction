# รายชื่อ Port (จากที่คุณให้)
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

# ใช้ข้อมูลจริงสร้าง Freight Cost Max ต่อ Port
if "Freight Cost Max" in available_features:
    port_max = df_model.groupby("Port")["Freight Cost Max"].max()
else:
    port_max = None

# เดือนอนาคต (1 เดือน)
future_dates = pd.date_range(start="2025-12-01", end="2025-12-31", freq="MS")

# สร้าง DataFrame: Port × Month (ไม่มี Mode)
future_df = pd.DataFrame(
    [(p, d.year, d.month) for p in port_list for d in future_dates],
    columns=["Port", "Year", "Month"]
)

# Mapping ค่า Freight Cost Max ต่อ Port
if port_max is not None:
    future_df["Freight Cost Max"] = 0.27 * future_df["Port"].map(port_max)

future_df
