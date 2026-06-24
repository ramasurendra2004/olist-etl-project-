import pandas as pd
order_items = pd.read_csv('data\olist_order_items_dataset.csv')

print('='*50)
print("First 5 Rows:")
print('='*50)
print(order_items.head())

print('='*50)
print("Info")
print('='*50)
print(order_items.info())

print('='*50)
print("Dataset shape")
print('='*50)
print(order_items.shape)

print('='*50)
print("Column Names")
print('='*50)
print(order_items.columns)

print('='*50)
print("Missing values")
print('='*50)
print(order_items.isnull().sum())

print('='*50)
print("Duplicated values")
print('='*50)
print(order_items.duplicated().sum())

print('='*50)
print("Unique values")
print('='*50)
print(order_items.nunique())