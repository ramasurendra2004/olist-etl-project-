import pandas as pd
orders = pd.read_csv('data\olist_orders_dataset.csv')

print('='*50)
print("First 5 Rows:")
print('='*50)
print(orders.head())

print('='*50)
print('Info')
print('='*50)
print(orders.info())

print('='*50)
print('Coloumn Names')
print('='*50)
print(orders.columns)

print('='*50)
print('Dataset shape')
print('='*50)
print(orders.shape)

print('='*50)
print('Missing values')
print('='*50)
print(orders.isnull().sum())

print('='*50)
print('Duplicated values')
print('='*50)
print(orders.duplicated().sum())

print('='*50)
print('Unique values')
print('='*50)
print(orders.nunique())

print('='*50)
print('Describe')
print('='*50)
print(orders.describe())

print('='*50)
print('Order status distribution')
print('='*50)
print(orders.order_status.value_counts())

print('='*50)
print('Transformations')
print('='*50)
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

print('='*50)
print('New Info')
print('='*50)
print(orders.info())

#creating delivery days column

orders['delivery_days'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days

print(orders.head())
print(orders.info())