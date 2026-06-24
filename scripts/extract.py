import pandas as pd

customers = pd.read_csv("data/olist_customers_dataset.csv")

print("First 5 Rows:")
print(customers.head())

print("\nInfo:")
print(customers.info())

print("="*50)
print("Dataset Shape")
print("="*50)
print(customers.shape)

print("="*50)
print("Coloumn Names")
print("="*50)
print(customers.columns)

print("="*50)
print("Missing Values")
print("="*50)
print(customers.isnull().sum())

print("="*50)
print("DUplicated Values")
print("="*50)
print(customers.duplicated().sum())

print("="*50)
print("Unique Values")
print("="*50)
print(customers.nunique())

print("="*50)
print("Transformations")
print('='*50)
customers['customer_city'] = customers['customer_city'].str.title()

print(customers.head)
