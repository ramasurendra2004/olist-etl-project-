import pandas as pd
customers = pd.read_csv("data/olist_customers_dataset.csv")
orders = pd.read_csv("data/olist_orders_dataset.csv")
order_items = pd.read_csv("data/olist_order_items_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
sellers = pd.read_csv("data/olist_sellers_dataset.csv")
payments = pd.read_csv("data/olist_order_payments_dataset.csv")
print("All Dataframes Loaded")

print("="*50)
print(" customer table Transformations")
print('='*50)
customers['customer_city'] = customers['customer_city'].str.title()

print(customers.head())

print("="*50)
print("orders table Transformations")
print('='*50)

# te date columns are shown as strings in info so we need to convert them to datetime
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

print("="*50)
print("orders_items table Transformations")
print('='*50)

order_items['shipping_limit_date'] = pd.to_datetime(order_items['shipping_limit_date'])

# Need to create total amount column
order_items['total_amount'] = order_items['price'] + order_items['freight_value']

# create fright percentage

order_items['freight_percentage'] = (order_items['freight_value'] / order_items['price']) * 100

print("="*50)
print("Product table Transformations")
print('='*50)

# filling missing values in categories
products['product_category_name'] = products['product_category_name'].fillna('unknown')

#filling missing dimensions

products['product_height_cm'] = products['product_height_cm'].fillna(products['product_height_cm'].median())
products['product_length_cm'] = products['product_length_cm'].fillna(products['product_length_cm'].median())
products['product_weight_g'] = products['product_weight_g'].fillna(products['product_weight_g'].median())
products['product_width_cm'] = products['product_width_cm'].fillna(products['product_width_cm'].median())

#craeting productvolume column
products['product_volume_cm3'] = products['product_height_cm'] * products['product_length_cm'] * products['product_width_cm']

print("="*50)
print("Seller table Transformations")
print('='*50)

sellers['seller_city'] = sellers['seller_city'].str.title()

print("="*50)
print("Payment table Transformations")
print('='*50)

#changing not_defineed to unknown in payment_type
payments['payment_type'] = payments['payment_type'].replace('not_defined', 'unknown')

#creating emi flag
payments['is_installments'] = (payments['payment_installments'] > 1)

print("="*50)
print("All Dataframes Transformed")
print('='*50)

print("Products Null Values")
print(products.isnull().sum())

print("Orders Data Types")
print(orders.dtypes)

#saving the cleaaned datesets

customers.to_csv(
    "output/customers_clean.csv",
    index=False
)

orders.to_csv(
    "output/orders_clean.csv",
    index=False
)

order_items.to_csv(
    "output/order_items_clean.csv",
    index=False
)

products.to_csv(
    "output/products_clean.csv",
    index=False
)

sellers.to_csv(
    "output/sellers_clean.csv",
    index=False
)

payments.to_csv(
    "output/payments_clean.csv",
    index=False
)

print("Cleaned datasets saved successfully!")