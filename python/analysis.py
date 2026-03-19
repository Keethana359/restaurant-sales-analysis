
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("tips.csv")

# Display data
print(df.head())
print(df.info())

# Rename columns (for business clarity)
df.rename(columns={
    'total_bill': 'total_sales',
    'tip': 'tip_amount',
    'size': 'customer_count'
}, inplace=True)

# Check missing values
print(df.isnull().sum())

# Create new columns
df['tip_percentage'] = (df['tip_amount'] / df['total_sales']) * 100

# Convert categorical columns
df['day'] = df['day'].astype('category')
df['time'] = df['time'].astype('category')

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# ======================
# 📊 Exploratory Analysis
# ======================

# Total sales by day
sales_by_day = df.groupby('day')['total_sales'].sum()
print(sales_by_day)

sales_by_day.plot(kind='bar', title='Sales by Day')
plt.show()

# Average tip percentage by time
tip_by_time = df.groupby('time')['tip_percentage'].mean()
print(tip_by_time)

tip_by_time.plot(kind='bar', title='Tip % by Time')
plt.show()

# Top 10 highest bills
top_sales = df.sort_values(by='total_sales', ascending=False).head(10)
print(top_sales)

# Correlation
print(df[['total_sales', 'tip_amount', 'customer_count']].corr())
