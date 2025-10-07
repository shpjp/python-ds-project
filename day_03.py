import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("ds/Salary_Data.csv")

X = data[['YearsExperience']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

data['PredictedSalary'] = model.predict(X)

print("Model Coefficient(slope)", round(model.coef_[0], 2))
print("Model base salary ", round(model.intercept_, 2))

plt.scatter(data['YearsExperience'], data['Salary'], color='blue', label='Actual Salary')
plt.plot(data['YearsExperience'], data['PredictedSalary'], color='red', label='Predicted Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()