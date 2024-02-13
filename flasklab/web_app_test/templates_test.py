from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template("index.html")

@app.route('/rand')
def display_sentence():
  conn = psycopg2.connect(
  host="localhost",
  port=5432,
  database="feutsopm",
  user="feutsopm",
  password="java255expo"
  )

  curr = conn.cursor()
  curr.execute("SELECT city FROM cities")
  city_rows = curr.fetchall()
  city_list = [row[0] for row in city_rows]
  
  name_list = ['Jasmine', 'Sam', 'Liz', 'Talia', 'Cecilia', 'Amanda']
  adjective_list = ['Beautiful', 'Sage', 'Brave', 'Wise', 'Curious']

  selected_city = random.choice(city_list)
  selected_name = random.choice(name_list)
  selected_adjective = random.choice(adjective_list)
  selected_year = random.randint(1924,2024)

  conn.commit()
  conn.close()
  
  return render_template("random.html", name = selected_name, adjective = selected_adjective, city = selected_city, year = selected_year)

if __name__ == '__main__':
  my_port = 5125
  app.run(host='0.0.0.0', port = my_port)
