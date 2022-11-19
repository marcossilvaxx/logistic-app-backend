import sys
import psycopg2 as p
import config

sql_file = sys.argv[1]

with open(sql_file) as sql:
  query = sql.read()

try:
  conn = p.connect(
    user = config.POSTGRES_USER,
    password = config.POSTGRES_PASSWORD,
    host = config.POSTGRES_HOST,
    port = config.POSTGRES_PORT,
    database = config.POSTGRES_DB,
  )

  cursor = conn.cursor()
  cursor.execute(query)
  
  conn.commit()
  
  print("Tables created successfully");

except p.Error as error:
  print(f'There was an error with the database operation: {error}')
except Exception as error:
  print('There was an unexpected error {error}')
finally:
  if conn:
    cursor.close()
    conn.close()