import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

product_data = pd.read_sql("""
SELECT *
  FROM products;
""", conn)

#print(product_data)

product_name_and_code = pd.read_sql("""
SELECT productName, productCode
  FROM products;
""", conn).tail(6)

#print(product_name_and_code)

product_code_and_product_name= pd.read_sql("""
SELECT productCode, productName
  FROM products;
""", conn).tail(5)
#print(product_code_and_product_name)

product_line = pd.read_sql("""
SELECT productName, productLine 
      CASE
      WHEN productLine = "Planes" THEN "Plane"
      ELSE "Not Plane"
      END AS Planes
  FROM products;
  """, conn)
print(product_line)