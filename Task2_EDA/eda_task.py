# Required Libraries Import Karein
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset Load Karein (Seaborn ka built-in Titanic dataset use kar rahe hain)
print("--- DATASET LOADING ---")
df = sns.load_dataset('titanic')
print(df.head()) # Pehli 5 rows dekhne ke liye

# 2. Data Structure aur Info Check Karein
print("\n--- DATA STRUCTURE & INFO ---")
print(df.info()) # Variables, data types, aur non-null counts ke liye
print("\nShape of Dataset (Rows, Columns):", df.shape)

# 3. Missing Values aur Data Issues Check Karein
print("\n--- MISSING VALUES CHECK ---")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# 4. Summary Statistics (Statistical Analysis)
print("\n--- SUMMARY STATISTICS ---")
print(df.describe())

# 5. Trends, Patterns aur Visualization
print("\n--- GENERATING VISUALIZATIONS ---")

# Visualization 1: Survival count based on Class
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='class', hue='survived')
plt.title('Survival Count by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

# Visualization 2: Correlation Heatmap (Patterns aur Anomalies ke liye)
plt.figure(figsize=(8, 6))
# Numeric columns ki correlation nikal rahe hain
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

print("\nTask 2 EDA successfully completed!")
