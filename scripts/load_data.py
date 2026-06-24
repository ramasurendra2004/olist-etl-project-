from sqlalchemy import create_engine
from sqlalchemy.engine import URL

connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Ram@rocky143",
    host="localhost",
    database="olist_etl"
)

engine = create_engine(connection_url)

conn = engine.connect()

print("Database Connected Successfully!")

conn.close()

import pandas as pd



""" products= pd.read_csv('output/products_clean.csv')
products.to_sql(
    name ='products',
    con= engine,
    if_exists ='append',
    index=False
) 
print('products loaded successfully')

sellers= pd.read_csv('output/sellers_clean.csv')
sellers.to_sql(
    name = 'sellers',
    con= engine,
    if_exists ='append',
    index= False
)




print('sellers loaded successfully')

orders = pd.read_csv(
    "output/orders_clean.csv"
)

orders.to_sql(
    name="orders",
    con=engine,
    if_exists="append",
    index=False
)

print("Orders Loaded Successfully!") 

payments = pd.read_csv('output/payments_clean.csv')

payments.to_sql(
    name='payments',
    con=engine,
    if_exists ='append',
    index= False
)

print('payments loaded successfully')"""

order_items = pd.read_csv(
    "output/order_items_clean.csv"
)

order_items.to_sql(
    name="order_items",
    con=engine,
    if_exists="append",
    index=False
)

print("Order Items Loaded Successfully")



