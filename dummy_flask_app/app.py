import requests
from  flask import Flask, render_template, request, jsonify
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
    df = form_data['date_from']
    dt = form_data['date_to']
    ff = form_data['city_from']
    ft = form_data['city_to']
    dff = datetime.datetime.strptime(df,"%Y-%m-%d").strftime("%d/%m/%Y")
    dtf = datetime.datetime.strptime(dt,"%Y-%m-%d").strftime("%d/%m/%Y")
    noa = form_data['Passengers']
    queryUrl = flightquery(ff, ft , dff, dtf, noa)
    r = requests.get(queryUrl)
    # print (queryUrl)
    json_object = r.json()
    endpointAirlines = 'https://api.skypicker.com/airlines'
    resp = requests.get(endpointAirlines)
    airlineList = resp.json()
    # print(airlineList.content)

    if json_object['data'] == []:
        return render_template("no_flights.html")
    else:
       flights = (json_object['data'])
    # flights = list(map(lambda f: f.merge({'dTimeUTC': datetime.datetime.fromtimestamp(f['dTimeUTC']})), flights[0:6] ))
    for flight in flights[0:6]:
        flight['dTimeUTC'] = datetime.datetime.fromtimestamp(flight['dTimeUTC'])
        flight['aTimeUTC'] = datetime.datetime.fromtimestamp(flight['aTimeUTC'])
        airline_code = flight['airlines'][0]

        for airline in airlineList:
            if airline["id"] == airline_code:
                flight['airline_name'] = airline["name"]
                break

        flight['airlines'][0] = "https://images.kiwi.com/airlines/64x64/"+flight['airlines'][0]+".png"

    return  render_template('bookflights.html', flights=flights[0:6])

def flightquery(flyFrom, flyTo, dateFrom, dateTo, numberOfAdults):
    endpoint = "https://api.skypicker.com/flights?"
    requestString=endpoint+"flyFrom="+flyFrom+"&to="+flyTo+"&dateFrom="+dateFrom+"&dateTo="+dateTo+"&adults="+numberOfAdults+"&max_stopovers=0&partner=picky&limit=30&sort=price&asc=1"
    return requestString
#Weather
@app.route('/temperature', methods=['POST'])
def temperature():
    cityname = request.form['city']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=1d123b8e7211f587219d8da83fe28ab6')
    # "appid":"1d123b8e7211f587219d8da83fe28ab6"
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = (temp_k - 273.15)
    temp_c_rounded = round(temp_c, 2)
    return render_template('temperature.html', city=cityname, temp=temp_c_rounded)

if __name__ == "__main__":
    app.run(debug=True)
