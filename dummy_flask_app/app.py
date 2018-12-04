import requests
from  flask import Flask, render_template, request, jsonify
import babel
import datetime


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

@app.route("/bookflight",methods=["POST"])
def book_flight():
    form_data = request.form

    # return "All OK"
    # this line prints out the form to the browser
    # payload = {
    # 'flyFrom': form_data['city_from'], # default value is 'PRG'
    # 'to': form_data['city_to'],
    # 'dateFrom': form_data['dateFrom'],
    # 'dateTo': arrow.utcnow().shift(weeks=+3).format('DD/MM/YYYY'),
    # 'partner': 'picky' # default value is 'picky' use it for testing
    # }

    d = form_data['date_from']
    ff = form_data['city_from']
    ft = form_data['city_to']
    df = datetime.datetime.strptime(d,"%Y-%m-%d").strftime("%d/%m/%Y")
    noa = form_data['Passengers']
    queryUrl = flightquery(ff, ft , df, noa)
    response = requests.get(queryUrl)
    #jsonify(request.form.to_dict())
    # return jsonify(request.form.to_dict())
    # content2= (response.content).decode('utf-8')
    # content="".join(map(chr, response.content)).encode()
    return response.content
    # response.contecontent
#     return datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%d/%m/%Y")

def flightquery(flyFrom, flyTo, dateFrom, numberOfAdults):
    endpoint = "https://api.skypicker.com/flights?"
    requestString=endpoint+"flyFrom="+flyFrom+"&to="+flyTo+"&dateFrom="+dateFrom+"&adults="+numberOfAdults+"&max_stopovers=0&partner=picky"
    return requestString
if __name__ == "__main__":
    app.run(debug=True)
