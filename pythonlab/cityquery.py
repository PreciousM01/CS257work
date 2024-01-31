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
  curr.execute("SELECT lat, lon FROM cities WHERE city = %s", (city_name,))
  result = curr.fetchone()
  conn.commit()
  conn.close()
  return result or False

def largest_pop():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo")
  
  curr = conn.cursor()
  curr.execute("SELECT city FROM cities ORDER BY population DESC LIMIT 1")
  result = curr.fetchone()
  conn.commit()
  conn.close()
  return result
  
def main():
  city_name = 'northfield'
  location = get_location()
  if location:
    latitude, longitude = location
    print(f'The location of {city_name} is latitude: {latitude} and longitude: {longitude}')
  else:
    print(f'{city_name} is not found in the database')

  print(largest_pop(), " has the largest population")
    
if __name__ =="__main__":
    main()
