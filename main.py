from weather import Weather
from interface import GUI

App = GUI()
 
city = "Ottawa"#input("Enter the city: ")
api_key = "f213efb3fd42cf9b00fcd0cc2df00af7"

WeatherInfo = Weather(city, api_key)
print('ran through')