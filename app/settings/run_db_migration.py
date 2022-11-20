import sys
import psycopg2 as p
import config

def run():
  sql_file = sys.argv[1]

  with open(sql_file) as sql:
    query = sql.read()
    
    
  conn = None
  
  try:
    conn = p.connect(
      user = config.POSTGRES_USER,
      password = config.POSTGRES_PASSWORD,
      host = config.POSTGRES_HOST,
      port = config.POSTGRES_PORT,
      database = config.POSTGRES_DB,
    )
    
    print("Starting migration...")

    cursor = conn.cursor()
    cursor.execute(query)
    
    conn.commit()
    
    print("Tables created successfully")

  except p.Error as error:
    print(f'Migration - There was an error with the database operation: {error}')
  except Exception as error:
    print('Migration - There was an unexpected error {error}')
  finally:
    if conn:
      cursor.close()
      conn.close()
      
if __name__ == '__main__':
  run()