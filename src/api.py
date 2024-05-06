from flask import Flask, Response
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World from Index!</p>"


@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/training_data")
def training_data():
    data = pd.read_csv("data/auto-mpg.csv")
    return Response(data.to_json(), mimetype="application/json")
