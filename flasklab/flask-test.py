import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:teal">' + word1 + '</h1>'

@app.route('/add/<number1>/<number2>')
def my_addition(number1, number2):
    sum = int(number1) + int(number2)
    return str(sum)

    
@app.route('/pop/<abbr>')
def get_statepop(abbr):
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="feutsopm",
    user="feutsopm",
    password="java255expo"
    )
    
    curr = conn.cursor()
    sql= 'SELECT population FROM states2 WHERE code = %s'
    curr.execute(sql, (abbr,))
    statepop = str(curr.fetchone())
    print("The population of " + abbr + "is: ", statepop)
    conn.commit()
    conn.close()
    return statepop
    

if __name__ == '__main__':
    my_port = 5125
    app.run(host='0.0.0.0', port = my_port) 
