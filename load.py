import pandas as pd

df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")
print(df.head())
print(df.isnull().sum())
df = df.drop_duplicates()
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month
df['Year'] = df['Order_Date'].dt.year
df['Profit_Percentage'] = (df['Profit'] / df['Sales']) * 100
