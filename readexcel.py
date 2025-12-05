import pandas as pd
import numpy as np
 
#Read excel file
file_path=r'C:\projectinfosys\items.xlsx'
data=pd.read_excel(file_path)
 
print("First 5 rows")
print(data.head(5))
 
 
#clean columns 
data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")
col_to_clean=['quantity']
data['quantity']=(
    data['quantity'].replace([""," ","NA","N/A"],np.nan)
)
# convert to numeric
data['quantity']=pd.to_numeric(data['quantity'],errors='coerce')
 
data['quantity']=data['quantity'].fillna(444).astype(int)
 
print(data.columns)
print(data['quantity'].head(5))