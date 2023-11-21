# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
df = pd.read_csv('Data-Cleaning-cleaning.csv')

# Descriptive analysis
print(df.describe())
print(df.info())

# Average customer order
avg_order = df.groupby('customer_id')['order_id'].mean()

# Average shipping time
df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
df['shipping_time'] = (df['delivery_date'] - df['order_date']).dt.days
avg_shipping_time = df['shipping_time'].mean()

# Total sales growth
df['month'] = df['order_date'].dt.month
monthly_sales = df.groupby('month')['order_id'].sum()
sales_growth = monthly_sales.pct_change()

# Average sales per product
avg_sales_per_product = df.groupby('product_id')['order_id'].mean()

# Average sales per state
avg_sales_per_state = df.groupby('state')['order_id'].mean()

# Average price per product
avg_price_per_product = df.groupby('product_id')['price'].mean()

# Age range classification
bins = [0, 18, 30, 50, 70, 100]
labels = ['<18', '18-30', '30-50', '50-70', '70+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
age_range_classification = df['age_group'].value_counts()

print('Average Order:', avg_order)
print('Average Shipping Time:', avg_shipping_time)
print('Sales Growth:', sales_growth)
print('Average Sales per Product:', avg_sales_per_product)
print('Average Sales per State:', avg_sales_per_state)
print('Average Price per Product:', avg_price_per_product)
print('Age Range Classification:', age_range_classification)