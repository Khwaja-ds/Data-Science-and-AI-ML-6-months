import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("Salary_Data.csv")

# Features and Target
X = df[['YearsExperience']]
y = df['Salary']

# Split into train and test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open("salary_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as salary_model.pkl")

