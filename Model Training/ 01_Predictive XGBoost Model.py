import pandas as pd
from google.colab import files

# อัปโหลดไฟล์ Excel
uploaded = files.upload()

# อ่าน Sheet แรกในไฟล์
file_name = list(uploaded.keys())[0]
df = pd.read_excel(file_name, sheet_name=0)

df.head()
