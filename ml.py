import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.drop_duplicates()
df['Profit'] = df['Profit'].fillna(df['Profit'].mean())

X = df[['Quantity','Profit']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predicted Values:")
print(predictions)

score = model.score(X_test, y_test)
print("Model Accuracy:", score)

plt.figure()
plt.scatter(y_test, predictions)
plt.title("Actual vs Predicted Sales")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
