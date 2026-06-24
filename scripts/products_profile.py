import pandas as pd
products = pd.read_csv('data\olist_products_dataset.csv')

print('='*50)
print("First 5 Rows:")
print('='*50)
print(products.head())

print('='*50)
print("Info")
print('='*50)
print(products.info())

print('='*50)
print("Dataset shape")
print('='*50)
print(products.shape)

print('='*50)
print("Column Names")
print('='*50)
print(products.columns)

print('='*50)
print("Missing values")
print('='*50)
print(products.isnull().sum())

print('='*50)
print("Duplicated values")
print('='*50)
print(products.duplicated().sum())  

print('='*50)
print("Unique values")
print('='*50)
print(products.nunique())

print('='*50)
print("Describe")
print('='*50)
print(products.describe())