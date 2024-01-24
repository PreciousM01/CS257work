import psycopg2

def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="feutsopm",
        user="feutsopm",
        password="java255expo")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None
  
def create_tables():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo")

  cur = conn.cursor()
  sql = "CREATE TABLE states ( state text, abbreviation text);"
  sql = "CREATE TABLE cities ( city text, state text, population real, lat real, lon real);"
  cur.execute( sql )
  row = cur.fetchone()
  conn.commit()
  return row
