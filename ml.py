import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_excel(r"C:\Users\adija\Downloads\ecommerce_large_dataset.xlsx")

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.drop_duplicates()
df['Profit'] = df['Profit'].fillna(df['Profit'].mean())
#define feature and target
X = df[['Quantity']]
y = df['Sales']
#split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#create and train the model
model = LinearRegression()
model.fit(X_train, y_train)
#make predicitions
predictions = model.predict(X_test)
#evaluate model accuracy
print("Model Accuracy:",model.score(X_test,y_test))
#plot results
plt.scatter(X_test,y_test)
plt.plot(X_test,predictions)
plt.title("Linear regression (quantity vs sales)")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()
