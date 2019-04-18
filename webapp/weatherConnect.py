import time
import requests
import sqlalchemy
import json

#by jessie
def get_engine():
    try:
        engine = sqlalchemy.create_engine('mysql+pymysql://EnxiJessieMarian:SoftwareEngineering2019@dublinbikesdata.cmgmbuuwvwd0.eu-west-1.rds.amazonaws.com:3306/DublinBikesData', echo=True)
        return engine
    except:
        print("Connection to RDS instance failed")
        return None
     
def getWeather():  
    engine = get_engine()
    conn = engine.connect()  
    url = "http://api.openweathermap.org/data/2.5/weather?appid=ae679d7b6212a1a3daf681d0d843aa83&q=Dublin&units=metric"
    the_page = requests.get(url).json()
    print(the_page)
    weather = {
            'icon': "<img src = 'http://openweathermap.org/img/w/" + the_page['weather'][0]['icon'] + ".png' > " +
                    the_page['weather'][0]['description'], 'temperature': the_page['main']['temp'],
            'cloud-cover': the_page['clouds']['all'],
            'humidity': the_page['main']['humidity'],
            'wind-speed': the_page['wind']['speed'],
        }
    weatherJSON = json.dumps(weather)
    return weatherJSON
    engine.close()