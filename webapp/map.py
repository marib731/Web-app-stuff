from flask import Flask, g, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy


import json
import sqlite3
import pandas as pd




app = Flask(__name__, static_url_path='')
app.config.update(MAPS_APIKEY='AIzaSyD9RSjs_rAUX_KRiXxzUlNAL1aVzyZ6hs0',BIKE_API='8c88bf369a36af98d796377bc7d0defaf5bc562e') 
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://EnxiJessieMarian:SoftwareEngineering2019@{dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com}/DublinBikesData'
#the above aws app config was added on sat. not sure if ok
#https://stackoverflow.com/questions/14850341/connect-to-aws-rds-mysql-database-instance-with-flask-sqlalchemy
#db=SQLAlchemy(application) #seems to be working. Remeber that all worked before this line + one on top added
app.run(debug=True)
SQLALCHEMY_DATABASE_URI = 'mysql://EnxiJessieMarian:SoftwareEngineering2019@{dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com}/DublinBikesData'
SQLAlchemy_TRACK_MODIFICATIONS = False

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

def get_db():
	db=getattr(g, '_database', None)
	if db is None:
        	db = g._database = sqlite3.connect('mysql://EnxiJessieMarian:SoftwareEngineering2019@{dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com}/DublinBikesData')
	return db

@app.route("/")
@app.route("/home")	
def home():
    return render_template('home.html', posts=posts)

    
@app.route("/stations")
#def stations():
#	    return render_template('stations.html', title="stations")

def get_stations():     
	conn = get_db()
	rows = cur.execute("SELECT * from stations;")
	for row in rows:
	 stations.append(dict(row))
	 return jsonify(stations=stations)

@app.route("/maps")
def root():
    return render_template('maps.html', MAPS_APIKEY=app.config["MAPS_APIKEY"]) 


 
@app.route("/marker")
def marker():
    return render_template('maps.html', MAPS_APIKEY=app.config["MAPS_APIKEY"], BIKE_API=app.config["BIKE_API"])    

@app.route("/about")
def about():
	    return render_template('about.html', title="About")
