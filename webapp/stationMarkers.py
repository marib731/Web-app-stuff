import requests
import json

def getStations():   
    url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=166048e0e00bbc76dd9a53d07bab98427b29d1e0"
    the_page = requests.get(url).json()
    stationLocations = {}
    for row in the_page:
        stationLocations[row['number']] = [row['position']['lat'], row['position']['lng']]
        #conn.execute()
    stationLocationsJSON = json.dumps(stationLocations)
    return stationLocationsJSON


