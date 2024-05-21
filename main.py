from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/checkweather", methods=['POST','GET'])
def weather():
    error = None