import pandas as pd
#step-1: Load the dataset from excel file
df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")
#step-2: Display first 5 rows to understand structure
print(df.head())
#step-3: check for missing values in each column
print(df.isnull().sum())
#step-4: Remove duplicates records
df = df.drop_duplicates()
#step-5: to convert 'order_Date' column to datetime format
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
#step-6:extract month from order_Date for trend analysis
df['Month'] = df['Order_Date'].dt.month
df['Year'] = df['Order_Date'].dt.year
#step-6:create new feature for profit percentage
df['Profit_Percentage'] = (df['Profit'] / df['Sales']) * 100
