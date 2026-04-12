import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")

print(df.head())
print(df.info())
print(df.describe())

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.drop_duplicates()
df['Profit'] = df['Profit'].fillna(df['Profit'].mean())

df['Month'] = df['Order_Date'].dt.month
df['Year'] = df['Order_Date'].dt.year
df['Profit_Percentage'] = (df['Profit'] / df['Sales']) * 100

plt.figure()
df['Sales'].plot(kind='hist', bins=10)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

plt.figure()
df['Quantity'].plot(kind='hist', bins=10)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df['Sales'], df['Profit'])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
