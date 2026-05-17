# ===== DATA ANALYSIS PROJECT =====
# Goal: Analyze a dataset, clean it, and generate summary statistics

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv("C:/Users/megha/Desktop/python/data.csv")



# Quick overview
print("=== Dataset Info ===")
print(df.info())
print("\n=== First 5 Rows ===")
print(df.head())

# 2. Clean Data
# Drop duplicates
df = df.drop_duplicates()

# Fill missing values (example: numeric columns with mean, categorical with mode)
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 3. Filter & Transform
# Example: filter rows where age > 25
if 'age' in df.columns:
    filtered_df = df[df['age'] > 25]
    print("\n=== Filtered Rows (age > 25) ===")
    print(filtered_df.head())

# Example: create new column
if 'income' in df.columns and 'household_size' in df.columns:
    df['income_per_capita'] = df['income'] / df['household_size']

# 4. Group & Aggregate
if 'category' in df.columns and 'sales' in df.columns:
    grouped = df.groupby('category')['sales'].mean().reset_index()
    print("\n=== Average Sales by Category ===")
    print(grouped)

# 5. Summary Statistics
print("\n=== Summary Statistics ===")
print(df.describe())

# Value counts (example: category column)
if 'category' in df.columns:
    print("\n=== Category Counts ===")
    print(df['category'].value_counts())

# 6. Optional Graphs
if 'age' in df.columns:
    df['age'].hist(bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

if 'category' in df.columns and 'sales' in df.columns:
    grouped.plot(kind='bar', x='category', y='sales', legend=False)
    plt.title("Average Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Average Sales")
    plt.show()
