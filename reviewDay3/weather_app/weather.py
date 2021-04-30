from threading import Thread
import json
from urllib.request import urlopen
import time

class TempGetter(Thread):
    def __init__(self, city):
        """
        The __init__ method initializes the TempGetter class
        Takes a 'city' parameter
        """
        super().__init__()
        self.city = city
        self.temperature = -99

    def run(self):
        """
        The run method is invoked when this class is the target of a thread
        """
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']

def getWeather(cities=['athlone', 'galway']):
    """
    the getWeather method takes a list of cities and returns the temperature for each city.

    """
    threads = [TempGetter(c) for c in cities]
    start = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for thread in threads:
        return (thread.temperature)

# if module is run as a unit, execute tests
if __name__ == '__main__':
    import doctest
    # doctest.testmod(verbose = True) # comment out for profiling
    getWeather()