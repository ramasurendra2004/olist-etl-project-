import pandas as pd
payments = pd.read_csv('data\olist_order_payments_dataset.csv')

print('='*50)
print("First 5 Rows:")
print('='*50)
print(payments.head())

print('='*50)
print("Info:")
print('='*50)
print(payments.info())

print('='*50)
print("Dataset shape")
print('='*50)
print(payments.shape)

print('='*50)
print("Column Names")
print('='*50)
print(payments.columns)

print('='*50)
print("Null values")
print('='*50)
print(payments.isnull().sum())

print('='*50)
print("Duplicated Values")
print('='*50)
print(payments.duplicated().sum())

print('='*50)
print("Unique Values")
print('='*50)
print(payments.nunique())

print('='*50)
print("Describe")
print('='*50)
print(payments.describe())

print('='*50)
print("Payment type count")
print('='*50)
print(payments['payment_type'].value_counts())
