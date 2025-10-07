
import numpy as np
import pandas as pd

np.random.seed(42)

yoe = np.random.uniform(0.5, 10, 100).round(2)
salary = (30000 + yoe * 6000 + np.random.normal(0, 4000, size=100)).round(2)
data = {'YearsExperience': yoe, 'Salary': salary}

df = pd.DataFrame(data)

# Now save safely
df.to_csv("ds/Salary_Data.csv", index=False)

print("Data saved to 'ds/Salary_Data.csv'")
