def test_query_one():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mlepinski",
    user="PreciousM01",
    password="Moonlovers28.")

cur = conn.cursor()
sql = "CREATE TABLE states ( state text, abbreviation text);"
sql = "CREATE TABLE cities ( city text, state text, population real, lat real, lon real);"
cur.execute( sql )
