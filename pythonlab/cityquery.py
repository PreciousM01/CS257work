import psycopg2

def get_location():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo")

  curr = conn.cursor()
  city_name = 'northfield'
  curr.execute("SELECT lat, lon FROM cities WHERE city = ?",(city_name))
  result = cur.fetchone()
  conn.commit()
  conn.close()
  return result or False

  location = get_location()
  if location:
    latitude, longitude = location
    print(f'The location of {city_name} is latitude: {latitude} and longitude: {longitude}')
  else:
    print("{city_name} is not found in the database")
  
def main():
    get_location()
    
if __name__ =="__main__":
    main()