import psycopg2

def connection_info():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo"
  )
  return conn

def get_location():
  conn = connection_info()
  curr = conn.cursor()
  city_name = 'northfield'
  curr.execute("SELECT lat, lon FROM cities WHERE city = %s", (city_name,))
  result = curr.fetchone()
  conn.commit()
  conn.close()
  return result or False

def largest_pop():
  conn = connection_info()
  curr = conn.cursor()
  curr.execute("SELECT city FROM cities ORDER BY population DESC LIMIT 1")
  result = curr.fetchone()
  if result:
    largest_city = result[0]
    print("The city with the largest population is:", largest_city)
    
  conn.commit()
  conn.close()

def smallest_sate_city():
  conn = connection_info()
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
  conn = connection_info()
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
      furthest_west = (name, longitude)
    if furthest_east == None or longitude > furthest_east[1]:
      furthest_east = (name, longitude)
    if furthest_north == None or latitude > furthest_north[1]:
      furthest_north = (name, latitude)
    if furthest_south == None or latitude < furthest_south[1]:
      furthest_south = (name, latitude)

  print("The city furthest to the West is:", furthest_west)
  print("The city furthest to the East is:", furthest_east)
  print("The city furthest to the North is:", furthest_north)
  print("The city furthest to the South is:", furthest_south)
  
  conn.commit()
  conn.close

def get_total_state_population():
  conn = connection_info()
  curr = conn.cursor()
  state_in = str(input("Enter the state whose total population you want to check:"))
  if len(state_in) == 2:
    curr.execute("SELECT state FROM states WHERE abbreviation= %s", (state_in,))
    state_in = curr.fetchone()

  curr.execute("SELECT city, population FROM cities WHERE state = %s", (state_in,))
  cities = curr.fetchall()
  total_pop = 0
  for city in cities:
    name, population = city
    total_pop += city[1]

  print(f'The total population is {total_pop} in ', state_in)
  conn.commit()
  conn.close()
    
  
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
  get_total_state_population()
    
if __name__ =="__main__":
    main()
