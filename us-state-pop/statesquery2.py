import psycopg2

def conn_info():
  conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="feutsopm",
        user="feutsopm",
        password="java255expo"
  )
  return conn

def connection_text():
  conn = conn_info()
  if conn is not None:
    print('Connection worked')
  else:
    print('Connection unsuccessful')
  return None

  def state_proportions():
    conn = conn_info()
    curr = conn.cursor()
    sql = " SELECT code, state_name, city, population, state_population FROM states JOIN states2 WHERE state_name = state"
