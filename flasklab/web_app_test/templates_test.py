from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flaks(__name__)

@app.rout('/')
def welcome():
  return render_template("index.html")


