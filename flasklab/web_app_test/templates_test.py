from flask import Flask
from flask import render_template
import random

app = Flaks(__name__)

@app.rout('/')
def welcome():
  return render_template("index.html")


