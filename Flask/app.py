import datetime
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/gm")
def gm():
    return "Good Morning"

@app.route("/ge")
def ge():
    return "Good Evening"

@app.route("/date")
def date():
    from datetime import date
    today = date.today()

    return ("This is the today's Date {}".format(today))

@app.route('/req')    
def request_input():
    data = request.args.get('x')
    return "this is the input given by the user {}".format(data)
@app.route('/hello')
def govnid():
    return "Govind Bhai"

if __name__ == "__main__":
    app.run(debug=True)