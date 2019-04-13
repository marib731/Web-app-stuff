from flask import Flask, g, render_template, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import json
import sqlite3
import logging
import pandas as pd




app = Flask(__name__, static_url_path='')
app.config.update(MAPS_APIKEY='AIzaSyD9RSjs_rAUX_KRiXxzUlNAL1aVzyZ6hs0',BIKE_API='8c88bf369a36af98d796377bc7d0defaf5bc562e') 
 # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData'
engine = create_engine('mysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData', echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)


class Station(Base):
	__tablename__ = 'DublinBikesData'
	__tableargs__ = {'autoload': True}






posts=[
{
	'author':'Mini',
	'title':'First thingy',
	'content':'First thingy content',
	'date_posted':'today'
},
{
	'author':'Rupert',
	'title':'Second thingy',
	'content':'Second thingy content',
	'date_posted':'today'
}
]


def loadsession():
	metadata = Base.metadata
	Session = sessionmaker(bind=engine)
	session = Session()
	return session

@app.route("/")
@app.route("/home")	
def home():
    return render_template('home.html', posts=posts)

    
@app.route("/stations")
def stations():
	session = loadsession()
	all_stations = session.query(Station.StationID).distinct()
	station_list=[]
	for station in all_stations:
		station_list.append(session.query(Station).filter_by(StationID=station.StationID).first())
	return render_template('stations.html', title="stations", stations=station_list)

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

@app.route("/maps")
def root():
    return render_template('maps.html', MAPS_APIKEY=app.config["MAPS_APIKEY"]) 

@app.route("/x")
def x():
    return render_template('x.html', MAPS_APIKEY=app.config["MAPS_APIKEY"]) 
 
@app.route("/marker")
def marker():
    return render_template('maps.html', MAPS_APIKEY=app.config["MAPS_APIKEY"], BIKE_API=app.config["BIKE_API"])    

@app.route("/about", methods=['GET'])
def about():

	    return render_template('about.html', title="About")
# @app.route('/b')
# def bikes():
# 	db=