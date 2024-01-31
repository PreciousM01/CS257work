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
    print("The city with the smallest population in Minnesota is: ", smallest_statecity)

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
  smallest_state_city()
    
if __name__ =="__main__":
    main()
