"""
📊 Project: Product Data Cleaning Pipeline
Author: Joe Nganu
Description:
Cleans and prepares messy product data for analysis and reporting.
"""

import pandas as pd
from datetime import datetime

# 1️⃣ Load the raw CSV
df = pd.read_csv('raw_product_data.csv')

# 2️⃣ Clean column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# 3️⃣ Clean product names
df['product_name'] = df['product_name'].str.strip().str.lower().str.replace(r'[^a-z\s]', '', regex=True)

# 4️⃣ Remove £ symbol and convert to numeric
df['price'] = df['price'].astype(str).str.replace('£', '', regex=False)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 5️⃣ Fill missing prices with mean
df['price'].fillna(round(df['price'].mean(), 2), inplace=True)

# 6️⃣ Handle missing categories
df['category'].fillna('uncategorised', inplace=True)
df['category'] = df['category'].str.lower().str.strip()

# 7️⃣ Convert release_date to proper format
df['release_date'] = pd.to_datetime(df['release_date'], dayfirst=True, errors='coerce')
df['release_date'] = df['release_date'].dt.strftime('%Y-%m-%d')

# 8️⃣ Export cleaned dataset
df.to_excel('Cleaned_Product_Data.xlsx', index=False)

print("✅ Product data cleaned successfully – file saved as 'Cleaned_Product_Data.xlsx'")
