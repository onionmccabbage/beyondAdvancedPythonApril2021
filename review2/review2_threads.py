from threading import Thread
import json
import requests
import time

# CITIES = [
#     'Athlone', 'Dublin', 'Galway', 'Belfast', 
#     'London', 'Cork', 'Lund', 'Kista'
# ]
CITIES = [
    'Athlone', 'Canberra', 'london', 'athens'
]
# CITIES = ["Dublin","Cork","Limerick","Galway","Waterford","Drogheda","Kilkenny","Wexford","Sligo","Clonmel","Dundalk","Bray","Ennis","Tralee","Carlow","Naas","Athlone","Letterkenny","Tullamore","Killarney","Arklow","Cobh","Castlebar","Midleton","Mallow","Ballina","Enniscorthy","Wicklow","Cavan","Athy","Longford","Dungarvan","Nenagh","Trim","Thurles","Youghal","Monaghan","Buncrana","Ballinasloe","Fermoy","Westport","Carrick-on-Suir","Birr","Tipperary","Carrickmacross","Kinsale","Listowel","Clonakilty","Cashel","Macroom","Castleblayney","Kilrush","Skibbereen","Bundoran","Templemore","Clones","Newbridge","Mullingar","Balbriggan","Greystones","Leixlip","Tramore","Shannon","Gorey","Tuam","Edenderry","Bandon","Loughrea","Ardee","Mountmellick","Bantry","Boyle","Ballyshannon","Cootehill","Ballybay","Belturbet","Lismore","Kilkee","Granard"]

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        response = requests.get(url_template.format(self.city))
        data = json.loads(response.text)
        self.temperature = data['main']['temp']
        lon = 0
        lat = 52
        r = requests.get('https://www.google.co.uk/maps/place/{},{}'.format(lon, lat))
        print(r.text)

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

print(
    "Got {} reports in {} seconds".format(len(threads), time.time() - start))
