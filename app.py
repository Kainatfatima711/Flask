from flask import Flask, render_tempelate , request

app = Flask(__name__)


@app.route("/")
def myhome():
    return render_tempelate("index.html")


@app.route("/calculate", methods = ['POST'])
def mycalculate():
    units = int(request.form["units"])
    bill = units * 5
    if units <= 100:
        message = "Great! You are an energy saver!"
    elif units <= 200:
        message = "Not bad! Try saving a little more!"
    else :
        message = "Whao! Time to switch off some lights!"