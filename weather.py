import requests

ABSOLUTE_ZERO = 273.15

class Weather:

    def __init__(self, city, api_key):
        self.request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        self.response = requests.get(self.request_url)
        print(self.request_url)
        if self.response.status_code != 200: return False, print('')
        self.json_data = self.response.json()

    def get_temperature(self):
        temp = round(ABSOLUTE_ZERO - self.json_data['main']['temp'], 1)
        return f"{temp}°C"

    def get_location(self):
        return f"{self.json_data['name']}, {self.json_data['country']}"
     
