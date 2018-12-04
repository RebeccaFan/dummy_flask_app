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
    r = requests.get(queryUrl)
    # r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=fd38d62aa4fe1a03d86eee91fcd69f6e')
    json_object = r.json()
    # temp_k = float(json_object['main']['temp'])
    #jsonify(content())
    # return jsonify(request.form.to_dict())
    # content2= (response.content).decode('utf-8')
    # content="".join(map(chr, response.content)).encode()
    print ( json_object )
    if json_object['data'] == []:
        print( "CHECK OTHER DATE OR LOCATION")
    # ffrom = form_data['city_from']
    # fto = form_data['city_to']
    # date = float(json_object['main']['temp'])
    # airline_logo = "https://images.kiwi.com/airlines/64x64/"+"LO"+".png"
    return r.content
    # render_template("bookFlight.html", fl)
    # response.contejson
#     return datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%d/%m/%Y")

def flightquery(flyFrom, flyTo, dateFrom, numberOfAdults):
    endpoint = "https://api.skypicker.com/flights?"
    requestString=endpoint+"flyFrom="+flyFrom+"&to="+flyTo+"&dateFrom="+dateFrom+"&adults="+numberOfAdults+"&max_stopovers=0&partner=picky&limit=30&sort=price&asc=1"
    return requestString
if __name__ == "__main__":
    app.run(debug=True)
