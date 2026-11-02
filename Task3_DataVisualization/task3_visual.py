import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for professional charts
sns.set_theme(style="whitegrid")

print("--- 1. LOADING DATASET FOR VISUALIZATION ---")
# Using Seaborn's built-in 'tips' dataset for rich visual analysis
df = sns.load_dataset('tips')
print(df.head())

print("\n--- 2. GENERATING VISUALIZATIONS ---")

# Figure 1: Distribution of Total Bill (Histogram & KDE)
plt.figure(figsize=(8, 5))
sns.histplot(df['total_bill'], kde=True, color='purple', bins=20)
plt.title('Distribution of Total Bill Amounts', fontsize=14, fontweight='bold')
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig('total_bill_distribution.png', bbox_inches='tight')
plt.show()

# Figure 2: Relationship between Total Bill and Tip (Scatter Plot with Hue)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day', style='time', s=100, palette='deep')
plt.title('Total Bill vs Tip Amount by Day and Time', fontsize=14, fontweight='bold')
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Tip ($)', fontsize=12)
plt.savefig('bill_vs_tip_scatter.png', bbox_inches='tight')
plt.show()

# Figure 3: Average Tip by Day (Bar Plot)
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='day', y='tip', ci=None, palette='viridis')
plt.title('Average Tip Amount by Day of the Week', fontsize=14, fontweight='bold')
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Average Tip ($)', fontsize=12)
plt.savefig('average_tip_by_day.png', bbox_inches='tight')
plt.show()

print("\n--- VISUALIZATIONS SAVED SUCCESSFULLY ---")
