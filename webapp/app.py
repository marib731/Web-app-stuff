# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:46:02 2019

@author: Jessie

"""
import requests
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
import logging
import pandas as pd
from flask import Flask, g, render_template, url_for, jsonify, request, jsonify
from alertScraper import *
from stationMarkers import *
from weatherConnect import *
import numpy
import pickle
import json

app = Flask(__name__, static_url_path='')
app.config.update(MAPS_APIKEY='AIzaSyD9RSjs_rAUX_KRiXxzUlNAL1aVzyZ6hs0',BIKE_API='8c88bf369a36af98d796377bc7d0defaf5bc562e') 
 # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData'
engine = create_engine('mysql+pymysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData', echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)

app = Flask(__name__)

#  Enxi begin
@app.route('/stations')
def stations():
    stations_json = {}
    session = loadsession()
    all_stations = session.query(Station.StationID).distinct()
    station_list=[]
    for station in all_stations:
        station_list.append(session.query(Station).filter_by(StationID=station.StationID).first())
    try:
        with open("static/files/dublin.json") as stations_file:
            stations_json = json.load(stations_file)

    except Exception:
        pass
    return render_template('stations.html', stations_json=stations_json, title="stations", stations=station_list)
#  Enxi end


#marian
class Station(Base):
    __tablename__ = 'DublinBikesData'
    __tableargs__ = {'autoload': True}

def loadsession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session



@app.route("/station_id", methods=['POST'])
def get_station_id():
    session = loadsession()
    logging.info(request.args)
    stationid = int(request.form['station_id'])
    station = session.query(Station).filter_by(StationID=stationid).first()
    out_ = {}
    out_['address'] = station.address
    out_['bike_stands'] = station.bike_stands
    out_['available_bike_stands']= station.available_bike_stands
    out_['available_bikes'] = station.available_bikes
    out_['StationID'] = station.StationID
    return jsonify(out_)
#marian end



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
