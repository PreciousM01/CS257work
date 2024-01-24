import psycopg2

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
