# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:46:02 2019

@author: Jessie

"""

from flask import Flask, render_template, request, jsonify
from alertScraper import *
from stationMarkers import *
from weatherConnect import *
import numpy
import pickle
import json

app = Flask(__name__)

#  Enxi begin
@app.route('/stations')
def stations():
    stations_json = {}
    try:
        with open("static/files/dublin.json") as stations_file:
            stations_json = json.load(stations_file)

    except Exception:
        pass
    return render_template('stations.html', stations_json=stations_json)
#  Enxi end

@app.route('/route-planner')
def route():
    return render_template('route-planner.html')


@app.route('/getting-started')
def starting():
    return render_template('getting-started.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/my-account')
def login():
    return render_template('my-account.html')


@app.route("/index")
@app.route("/")
def root():
    return render_template("index.html")


@app.route('/api/db')
def get_db():
    return dbstationsAlerts()


@app.route('/api/aa')
def get_aa():
    return aaRoadAlerts()


@app.route('/api/stations')
def gettingStationLatLng():
    return getStations()


@app.route('/api/weather')
def gettingWeather():
    return getWeather()


#  Enxi begin

@app.route('/bikes_prediction')
def bikes_prediction():
    station_id = request.args.get('station_id')
    time_hour = int(request.args.get('time_hour'))
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?appid=ae679d7b6212a1a3daf681d0d843aa83&q=Dublin&units=metric')
    weathers = r.json()
    time_week = time.strftime("%w", time.localtime())
    weather_detalis = weathers["list"]
    temp = weather_detalis[0]['main']['temp']
    wind = weather_detalis[0]['wind']['speed']
    des = weather_detalis[0]['weather'][0]['main']
    weather_Drizzle = 0
    weather_Rain = 0
    weather_Snow = 0

    if des == 'Drizzle':
        weather_Drizzle = 1
    elif des == 'Rain':
        weather_Rain = 1
    elif des == 'Snow':
        weather_Snow = 1

    f2 = 0
    try:
        with open("static/pickle/" + str(station_id) + ".pkl", "rb") as handle:
            print(time_hour, temp, wind, time_week, weather_Drizzle, weather_Rain, weather_Snow)
            model = pickle.load(handle)
            f2 = model.predict(
                numpy.array([[time_hour, temp, wind, time_week, weather_Drizzle, weather_Rain, weather_Snow]]))
    except:
        pass
    return str(f2.round()[0])

#  Enxi end
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
