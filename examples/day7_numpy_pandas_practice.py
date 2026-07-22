import pandas as pd
import numpy as np


marks = np.array([78, 92, 45, 88, 35])

print("NumPy Array:", marks)
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Marks After Bonus:", marks + 5)


df = pd.read_csv("data/student_scores.csv")

print("\nFirst 5 Rows")
print(df.head())

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

df["english_score"] = df["english_score"].fillna(df["english_score"].mean())

df["total_score"] = df["math_score"] + df["english_score"] + df["science_score"]
df["percentage"] = (df["total_score"] / 300) * 100

features = df[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
target = df["result"]

train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

X_train = train_data[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
y_train = train_data["result"]

X_test = test_data[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
y_test = test_data["result"]

print("\nCleaned Student Scores")
print(df[["name", "total_score", "percentage", "result"]])

print("\nSelected Features")
print(features.head())

print("\nTarget")
print(target.head())

print("\nTrain Test Split")
print("Training rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])
print("Training target values:")
print(y_train)
print("Testing target values:")
print(y_test)
