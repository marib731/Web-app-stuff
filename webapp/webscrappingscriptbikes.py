# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:51:29 2019

@author: Jessie
"""

import requests
import time
import sqlalchemy


def fix_data(row):
    row['StationID'] = row['number']
    del row['number']
    row['position_lat'] = row['position']['lat']
    row['position_lng'] = row['position']['lng']
    del row['position']
    return row
 
 
def get_engine():
    try:
        engine = sqlalchemy.create_engine('mysql+pymysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData', echo=True)
        return engine
    except:
        print("Connection to RDS instance failed")
        return None
     
def main():  
    engine = get_engine()
    conn = engine.connect()  
    while True:
        url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=166048e0e00bbc76dd9a53d07bab98427b29d1e0"
        the_page = requests.get(url).json()
        for row in the_page:
            if 'number' in row:
                row = fix_data(row)
            sql = "insert ignore into {table} ({columns}) values ({values});".format(table="DublinBikesData", columns=",".join(row.keys()), 
                                                                                   values=", ".join(["%s"] * len(row)))
            #sql = DublinBikesData.insert().\values(name=bindparam({columns}).format(columns=",".join(row.keys())
            conn.execute(sql, list(row.values()))
        
        print("Sleeping")
        time.sleep(6*60)
    engine.close()
     
if __name__ == '__main__':
    main()
