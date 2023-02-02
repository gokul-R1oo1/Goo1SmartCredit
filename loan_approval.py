# AI for Loan Approval - loan_approval.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load loan data
df = pd.read_csv("loan_data.csv")

# Define features and target variables
features = df.drop("Loan_Status", axis=1)
target = df["Loan_Status"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

# Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate the model
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)

# Use the model to make loan approval predictions
new_loan_data = [{"Loan_Amount": 5000, "Credit_History": 1, "Income": 60000},
                 {"Loan_Amount": 6000, "Credit_History": 0, "Income": 45000}]

new_loan_data = pd.DataFrame(new_loan_data)
predictions = clf.predict(new_loan_data)
print("Predictions:", predictions)
