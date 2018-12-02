import requests
from  flask import Flask, render_template, request, jsonify


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
    formvalues=[]
    form_data = request.form
    print(form_data['date_from'].format('DD/MM/YYYY'))
    # return "All OK"
    # this line prints out the form to the browser
    # payload = {
    # 'flyFrom': form_data['city_from'], # default value is 'PRG'
    # 'to': form_data['city_to'],
    # 'dateFrom': form_data['dateFrom'],
    # 'dateTo': arrow.utcnow().shift(weeks=+3).format('DD/MM/YYYY'),
    # 'partner': 'picky' # default value is 'picky' use it for testing
    # }
    return jsonify(request.form.to_dict())


# def flightquery():
#
#
# res = s.search_flights(**payload)
# endpoint = "https://api.skypicker.com/flights?flyFrom=PRG&to=LGW&dateFrom=18/11/2018&dateTo=12/12/2018&partner=picky"
# payload = {"dateFrom"=18/11/2018 & dateTo=12/12/2018 & partner=picky}
#
# response = requests.get(endpoint, params=payload)

if __name__ == "__main__":
    app.run(debug=True)
