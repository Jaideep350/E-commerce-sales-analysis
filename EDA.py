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
#last preprocessing step
df['Profit_Percentage'] = (df['Profit'] / df['Sales']) * 100
# Outlier Detection using IQR method

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
#calculate basic statistical measure
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()

print("Mean:", mean_sales)
print("Median:", median_sales)
#sales distribution histogram
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
