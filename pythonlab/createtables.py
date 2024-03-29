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
  cur.execute( sql)
  sql = "CREATE TABLE cities ( city text, state text, population int, lat real, lon real);"
  cur.execute( sql )
  conn.commit()

def main():
    test_connection()
    create_tables()
    
if __name__ =="__main__":
    main()
