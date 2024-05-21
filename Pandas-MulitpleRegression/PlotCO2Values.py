import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
 
# Load the data
df = pd.read_csv("data.csv")
 
# Separate features and target variable
X = df[['Weight', 'Volume']]
y = df['CO2']
 
# Standardize features
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
 
# Train the linear regression model
regr = linear_model.LinearRegression()
regr.fit(scaled_X, y)
 
# Scale the new data point
new_data = [[2300, 1.3]]
scaled_new_data = scaler.transform(new_data)
 
# Predict CO2 emission for the new data point
predicted_CO2 = regr.predict(scaled_new_data)
print("Predicted CO2 Emission:", predicted_CO2)
 
# Plotting
plt.scatter(X['Weight'], y, color='blue', label='Actual CO2')
plt.scatter(new_data[0][0], predicted_CO2, color='red', label='Predicted CO2', marker='x', s=100)
plt.xlabel('Weight')
plt.ylabel('CO2 Emission')
plt.title('Predicted CO2 Emission for New Data Point')
plt.legend()
plt.grid(True)
plt.show()
