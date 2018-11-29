import requests
from  flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template("project.html")

@app.route("/cold")
def cold():
    return render_template("cold-country.html")

@app.route("/hot")
def hot():
    return render_template("hot-country.html")
@app.route("/budget")
def budget():
    return render_template("on-budget.html")

if __name__ == "__main__":
    app.run(debug=True)
