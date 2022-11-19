import sys
import psycopg2 as p
import config
import os
import csv

def parse_csv_row(row):
  return ["0" if i == "" else i for i in row]

def insert_row(cursor, table, columns, data):
  formatted_columns = ", ".join(columns)
  
  formatted_args = ", ".join(["%s"] * len(columns))  
  
  query = f"INSERT INTO {table} ({formatted_columns}) VALUES ({formatted_args})"
  
  cursor.execute(query, parse_csv_row(data))

try:
  conn = p.connect(
    user = config.POSTGRES_USER,
    password = config.POSTGRES_PASSWORD,
    host = config.POSTGRES_HOST,
    port = config.POSTGRES_PORT,
    database = config.POSTGRES_DB,
  )

  cursor = conn.cursor()
  
  seed_files = ["companies.csv", "customers.csv", "orders.csv", "order_items.csv", "deliveries.csv"]
  
  for seed_file in seed_files:
    tablename = seed_file.split(".")[0]
    
    columns = []
    
    with open(f"seed_data/{seed_file}") as file:
      csvFile = csv.reader(file)
  
      for i, lines in enumerate(csvFile):
        if i == 0:
          columns = lines
        else:
          insert_row(cursor, tablename, columns, lines)
      print(f"{tablename} table loaded\n")
  
  conn.commit()

except p.Error as error:
  print(f'There was an error with the database operation: {error}')
except Exception as error:
  print(f'There was an unexpected error {error}')
finally:
  if conn:
    cursor.close()
    conn.close()