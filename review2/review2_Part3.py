from threading import Thread
import threading
import json
from urllib.request import urlopen
import time

CITIES = [
    'Athlone', 'Dublin', 'Galway', 'Belfast', 
    'London', 'Cork', 'Lund', 'Kista'
]
# CITIES = [
#     'Athlone', 'Dublin'
# ]
# CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]
lock = threading.Lock()
count = 0
weatherStructure = []

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        global count
        global weatherStructure
        lock.acquire()
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.description = data['weather'][0]['description']
        self.temperature = data['main']['temp']
        self.windSpeed = data['wind']['speed']
        self.windDirection = data['wind']['deg']
        self.lat = data['coord']['lat']
        self.lon = data['coord']['lon']

        # persist the weather data in a global structure
        weatherStructure.append({
            'city':self.city,
            'description':self.description,
            'temperature':self.temperature,
            'wind':{'speed':self.windSpeed, 'direction':self.windDirection},
            'lat':self.lat, 
            'lon':self.lon})
        count = count + 1

        # release the lock
        lock.release()

threads = [TempGetter(c) for c in CITIES]
start = time.time()
# first we kick off all the threads
for thread in threads:
    thread.start()

# now we wait for all the threads to complete
for thread in threads:
    thread.join()
    print(
        "it is {0.temperature:.0f}°C in {0.city}".format(thread))
    print('Number of responses: {}'.format(count))
    print('lat {0.lat}, lon {0.lon}'.format(thread))

print(
    "Got {} reports in {} seconds".format(len(threads), time.time() - start))
print (weatherStructure)
