import pandas as pd
sellers = pd.read_csv('data\olist_sellers_dataset.csv')

print('='*50)
print("First 5 Rows:")
print('='*50)
print(sellers.head())

print('='*50)
print("Info")
print('='*50)
print(sellers.info())

print('='*50)
print("Dataset shape")
print('='*50)
print(sellers.shape)

print('='*50)
print("Column Names")
print('='*50)
print(sellers.columns)

print('='*50)
print("Null values")
print('='*50)
print(sellers.isnull().sum())

print('='*50)
print("Duplicated Values")
print('='*50)
print(sellers.duplicated().sum())

print('='*50)
print("Unique values")
print('='*50)
print(sellers.nunique())

print('='*50)
print("Describe")
print('='*50)
print(sellers.describe())