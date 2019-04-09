import requests
import sqlalchemy
import json

def get_engine():
    try:
        engine = sqlalchemy.create_engine('mysql+pymysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData', echo=True)
        return engine
    except:
        print("Connection to RDS instance failed")
        return None
     
def getStations():  
    engine = get_engine()
    conn = engine.connect()  
    url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=166048e0e00bbc76dd9a53d07bab98427b29d1e0"
    the_page = requests.get(url).json()
    stationLocations = {}
    for row in the_page:
        stationLocations[row['StationID']] = [row['position']['lat'], row['position']['lng']]
        conn.execute()
    stationLocationsJSON = json.dumps(stationLocations)
    return stationLocationsJSON
    engine.close()
     
