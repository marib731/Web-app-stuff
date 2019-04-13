from flask import Flask, g, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import json
import sqlite3
import pandas as pd


app = Flask(__name__, static_url_path='')
app.config.from_object('config')

def connect_to_database():
	engine = create_engine('mysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData', echo=True)


def get_db():
	db = getattr(g, '_database', None)
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_to_database()
	return g.sqlite_db

def close_connection(exception):
	db = getattr(g, '_database', None)
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

@app.route("/")
def get_stations():
	engine = get_db()
	data = []
	sql = "SELECT available_bikes from DublinBikesData where StationID = {2}"
	rows = engine.execute(sql)
	for row in rows:
		data.append(dict(row))

	return jsonify(available=data) 

 