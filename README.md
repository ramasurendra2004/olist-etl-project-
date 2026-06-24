# Olist E-Commerce ETL Project

## 📌 Project Overview

This project implements an end-to-end **ETL (Extract, Transform, Load)** pipeline using **Python, Pandas, MySQL, SQLAlchemy, and PyMySQL** on the Olist Brazilian E-Commerce dataset.

The primary objective is to extract data from multiple CSV files, perform data cleaning and feature engineering, load the transformed data into a relational database, and generate business insights through SQL analytics.

---

## 🛠️ Tech Stack

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| Python     | ETL Development                  |
| Pandas     | Data Extraction & Transformation |
| MySQL      | Data Storage & Querying          |
| SQLAlchemy | Database Connectivity            |
| PyMySQL    | MySQL Driver                     |
| SQL        | Data Analysis                    |
| VS Code    | Development Environment          |

---

## 📂 Dataset Description

The project uses six datasets:

### 1. Customers

Contains customer demographic and location information.

**Columns:**

* customer_id
* customer_unique_id
* customer_zip_code_prefix
* customer_city
* customer_state

### 2. Orders

Contains order lifecycle and delivery information.

**Columns:**

* order_id
* customer_id
* order_status
* order_purchase_timestamp
* order_approved_at
* order_delivered_carrier_date
* order_delivered_customer_date
* order_estimated_delivery_date

### 3. Order Items

Contains product-level details for each order.

**Columns:**

* order_id
* order_item_id
* product_id
* seller_id
* shipping_limit_date
* price
* freight_value

### 4. Products

Contains product attributes and specifications.

**Columns:**

* product_id
* product_category_name
* product_name_length
* product_description_length
* product_photos_qty
* product_weight_g
* product_length_cm
* product_height_cm
* product_width_cm

### 5. Sellers

Contains seller information.

**Columns:**

* seller_id
* seller_zip_code_prefix
* seller_city
* seller_state

### 6. Payments

Contains order payment information.

**Columns:**

* order_id
* payment_sequential
* payment_type
* payment_installments
* payment_value

---

## 🔄 ETL Workflow

```text
CSV Files
    │
    ▼
Extract (Pandas)
    │
    ▼
Transform (Data Cleaning & Feature Engineering)
    │
    ▼
Load (MySQL Database)
    │
    ▼
SQL Analytics
```

---

## 🗄️ Database Schema

### Customers

**Primary Key**

* customer_id

### Orders

**Primary Key**

* order_id

**Foreign Key**

* customer_id → customers(customer_id)

### Products

**Primary Key**

* product_id

### Sellers

**Primary Key**

* seller_id

### Payments

**Foreign Key**

* order_id → orders(order_id)

### Order Items

**Foreign Keys**

* order_id → orders(order_id)
* product_id → products(product_id)
* seller_id → sellers(seller_id)

---

## 🧹 Data Transformations Performed

### Customers

* Standardized customer city names using Title Case.

**Example**

Before:

```text
sao paulo
```

After:

```text
Sao Paulo
```

---

### Orders

#### Date Conversion

Converted the following columns from string to datetime:

* order_purchase_timestamp
* order_approved_at
* order_delivered_carrier_date
* order_delivered_customer_date
* order_estimated_delivery_date

#### Feature Engineering

Created:

**delivery_days**

Formula:

```python
order_delivered_customer_date - order_purchase_timestamp
```

---

### Order Items

#### Date Conversion

Converted:

```python
shipping_limit_date
```

to datetime format.

#### Feature Engineering

Created:

**total_amount**

```python
price + freight_value
```

Created:

**freight_percentage**

```python
(freight_value / price) * 100
```

---

### Products

#### Missing Value Handling

Filled missing values in:

```python
product_category_name
```

using:

```python
Missing
```

#### Median Imputation

Applied median imputation to:

* product_height_cm
* product_length_cm
* product_weight_g
* product_width_cm

#### Feature Engineering

Created:

**product_volume**

```python
product_length_cm * product_width_cm * product_height_cm
```

---

### Sellers

* Standardized seller city names using Title Case.

---

### Payments

#### Data Cleaning

Replaced:

```python
not_defined
```

with:

```python
unknown
```

#### Feature Engineering

Created:

**is_installments**

```python
payment_installments > 1
```

---

## 📥 Data Loading

The transformed datasets were loaded into MySQL using:

```python
pandas.to_sql()
```

through SQLAlchemy and PyMySQL.

---

## 📊 Business Questions Solved

### Revenue Analysis

* Total Revenue Generated
* Revenue by Payment Type

### Customer Analysis

* Top States by Customers
* Top Cities by Customers

### Seller Analysis

* Top Sellers by Revenue
* Top Sellers by Number of Orders

### Product Analysis

* Top Products by Revenue
* Products with Highest Freight Cost

### Order Analysis

* Monthly Order Trend
* Average Delivery Time
* Order Status Distribution
* Percentage of Delivered Orders

---

## 📈 Sample SQL Insights

### Total Revenue

```sql
SELECT ROUND(SUM(payment_value),2) AS total_revenue
FROM payments;
```

### Monthly Order Trend

```sql
SELECT DATE_FORMAT(order_purchase_timestamp,'%Y-%m') AS month,
       COUNT(*) AS no_of_orders
FROM orders
GROUP BY month
ORDER BY month;
```

### Top Sellers by Revenue

```sql
SELECT seller_id,
       SUM(total_amount) AS revenue_generated
FROM order_items
GROUP BY seller_id
ORDER BY revenue_generated DESC
LIMIT 10;
```

---

## 🎯 Project Outcome

Successfully designed and implemented an end-to-end ETL pipeline capable of:

* Extracting data from multiple CSV sources
* Cleaning and transforming datasets
* Engineering business features
* Loading data into a relational database
* Performing analytical SQL queries
* Generating business insights

---

## 💡 Skills Demonstrated

* Python
* Pandas
* SQL
* MySQL
* SQLAlchemy
* PyMySQL
* ETL Development
* Data Cleaning
* Feature Engineering
* Relational Database Design
* Data Analysis
* SQL Query Optimization

---

## 🚀 Future Enhancements

* Build Power BI dashboards using the MySQL database
* Automate ETL execution using scheduling tools
* Deploy the pipeline using cloud services
* Implement incremental data loading
* Add data quality validation checks
