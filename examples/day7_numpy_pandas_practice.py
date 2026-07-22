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

print("\nCleaned Student Scores")
print(df[["name", "total_score", "percentage", "result"]])

print("\nSelected Features")
print(features.head())

print("\nTarget")
print(target.head())
