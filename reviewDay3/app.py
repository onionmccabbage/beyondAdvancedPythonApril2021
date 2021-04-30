# in windows console: set FLASK_ENV = development
# then server notices changes to files (just refresh the browser)'

from flask import Flask
from flask import render_template
import requests

# we need the weather module
import weather_app.weather as weather

app = Flask(__name__)
@app.route('/') 
def index(): 
  return render_template('index.html')

@app.route('/osm')
@app.route('/osm/<lon>/<lat>')
def osm(lon=-7.900, lat=53.429): 
    return render_template('osm_map.html', lon=lon, lat=lat)

# just get a static weather temperature
@app.route('/weather/')
def getWeather():
    city = 'athlone'
    country = 'ie'
    APIkey='APPID=48f2d5e18b0d2bc50519b58cce6409f1'
    url_str = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&{}'
    url = url_str.format(city, country, APIkey)
    data = requests.get(url).json()
    if 'main' in data:
        # self.temperature = data['main']['temp']
        return str(data['main']['temp'])

# use the weather module
@app.route('/weather/<c1>')
def getOneParamWeather(c1=False):
    # call weather module
    cities = [c1]
    temperature = weather.getWeather(cities)
    result = "In " + cities[0] + " it is " + str(temperature)
    # return temperature for chosen city
    return result

@app.route('/kitten/<w>/<h>')
def kitten(w,h): 
    return render_template('kitten.html', w=w, h=h)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run()