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
  if result:
    largest_city = result[0]
    print("The city with the largest population is:", largest_city)
    
  conn.commit()
  conn.close()

def smallest_sate_city():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo")

  curr = conn.cursor()
  fstate = 'Minnesota'
  curr.execute("SELECT city FROM cities WHERE state= %s ORDER BY population ASC LIMIT 1", (fstate,))
  result = curr.fetchone()
  smallest_statecity = result[0]
  if result:
    print("The city with the smallest population in Minnesota is:", smallest_statecity)

  conn.commit()
  conn.close()

def get_extreme_cities():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo")

  curr= conn.cursor()
  sql = 'SELECT city, lat, lon FROM cities'
  curr.execute(sql)
  cities = curr.fetchall()

  furthest_west = None
  furthest_east = None
  furthest_north = None
  furthest_south = None

  for city in cities:
    name, latitude, longitude = city
    if furthest_west == None or longitude < furthest_west[1]:
      further_west = (name, longitude)
    if further_east == None or longitude > further_east[1]:
      further_east = (name, longitude)
    if further_north == None or latitude > further_north[1]:
      further_north = (name, latitude)
    if further_south == None or latitude < further_south[1]:
      further_south = (name, latitude)

  print("The city furthest to the West is:", further_west)
  print("The city furthest to the East is:", further_east)
  print("The city furthest to the North is:", further_north)
  print("The city furthest to the South is:", further_south)
  
  conn.commit()
  conn.close
  
def main():
  city_name = 'Northfield'
  location = get_location()
  if location:
    latitude, longitude = location
    print(f'The location of {city_name} is latitude: {latitude} and longitude: {longitude}')
  else:
    print(f'{city_name} is not found in the database')

  largest_pop()
  smallest_sate_city()
  get_extreme_cities()
    
if __name__ =="__main__":
    main()
