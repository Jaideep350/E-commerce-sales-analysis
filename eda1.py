import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.drop_duplicates()
df['Profit'] = df['Profit'].fillna(df['Profit'].mean())

df['Month'] = df['Order_Date'].dt.month
#calculate correlation matrix
correlation = df[['Sales','Profit','Quantity']].corr()
#plot heat map
plt.figure()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()
#region wise sales aggregation
category_sales = df.groupby('Category')['Sales'].sum()
#bar chart for visualization
plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Region")
plt.ylabel("")
plt.show()
#monthly sales aggregation
monthly_sales = df.groupby('Month')['Sales'].sum()
#line chart for trend visualization
plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure()
df.boxplot(column='Sales')
plt.title("Boxplot for Sales")
plt.show()
#top 5 products based on sales
top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head()
#bar chart for top products
plt.figure()
top_products.plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

print(category_sales.sort_values(ascending=False))
print(region_sales.sort_values(ascending=False))
print(top_products)
