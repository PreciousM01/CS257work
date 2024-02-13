from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flaks(__name__)

@app.rout('/')
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

  curr = cursor.connect()
  city_list = curr.execute("SELECT city FROM cities")
  name_list = ['Jasmine', 'Sam', 'Liz', 'Talia', 'Cecilia', 'Amanda']
  adjective_list = ['Beautiful', 'Sage', 'Brave', 'Wise', 'Curious']

  selected_city = random.choice(city_list)
  selected_name = random.choice(name_list)
  selected_adjective = ramdom.choice(adjective_list)
  selected_year = random.randint(1924,2024)

  return render_template("random.html", selected_name, selected_adjective, selected_city, selected_year)
