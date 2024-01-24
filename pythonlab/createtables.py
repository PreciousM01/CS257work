import psycopg2

def test_query_one():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="Iwillreachthestars")

cur = conn.cursor()
sql = "CREATE TABLE states ( state text, abbreviation text);"
sql = "CREATE TABLE cities ( city text, state text, population real, lat real, lon real);"
cur.execute( sql )
