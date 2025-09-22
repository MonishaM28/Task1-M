
# Task 1: Data Cleaning & Preprocessing (Titanic Dataset)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Load Dataset
df = pd.read_csv(r"C:\Users\monisha\Downloads\Titanic-Dataset.csv")  # Place Titanic dataset in same folder
print("Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

# 2. Handle Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# 3. Encode Categorical Features
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])  # Male=1, Female=0
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# 4. Drop Irrelevant Columns
df.drop(columns=['Name', 'Ticket', 'PassengerId'], inplace=True)

# 5. Outlier Detection (Boxplots)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(df['Age'], ax=axes[0])
sns.boxplot(df['Fare'], ax=axes[1])
plt.savefig("outliers.png")
plt.close()

# Remove extreme outliers using IQR
for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] > upper, upper,
                np.where(df[col] < lower, lower, df[col]))

# 6. Normalize Numerical Features
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

print("Preprocessing Completed!")
print(df.head())

# Save cleaned dataset
df.to_csv("Titanic-Dataset_cleaned.csv", index=False)
