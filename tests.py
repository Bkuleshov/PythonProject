import unittest
import requests

botToken = "5341494742:AAGTtkY2hNDVTnsTSHPDmZsY_t4aUTA31eo"
apiKey = "bccc256b25008606026828a90cadfbf2"

class TestBot(unittest.TestCase):

    def test_timezone(self):
        cityName = 'Omsk'
        request = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': cityName, 'units': 'metric', 'APPID': apiKey}).json()
        self.assertEqual('6', str(int(request['timezone']) // 3600))
    
    def test_latitude(self):
        cityName = 'Omsk'
        request = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': cityName, 'units': 'metric', 'APPID': apiKey}).json()
        self.assertEqual('55', str(request['coord']['lat']))

if __name__ == '__main__':
    unittest.main()
