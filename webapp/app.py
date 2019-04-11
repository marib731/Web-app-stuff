# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:46:02 2019

@author: Jessie
"""

from flask import Flask, render_template
from alertScraper import *
from stationMarkers import *
from weatherConnect import *

app = Flask(__name__)

@app.route('/stations')
def stations():
    return render_template('stations.html')

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
