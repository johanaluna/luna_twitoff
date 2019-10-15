#import flask package. flask makes app objects.
from flask import Flask, render_template

#create Flask web server, makes the application
app = Flask(__name__)

#routes determine location
@app.route("/")

#Define simple function
def home():
    return render_template('home.html')

@app.route("/about")
def preds():
    return render_template('about.html')

@app.route("/luna1")
def example1():
    return render_template('luna1.html')

@app.route("/luna2")
def example2():
    return render_template('luna2.html')

@app.route("/luna3")
def example3():
    return render_template('luna3.html')

@app.route("/<int:numb>")
def example4(numb):
    fact = [x for x in range(1, numb+1) if numb%x==0]
    return "The factors of {} are {}".format(numb, fact)
