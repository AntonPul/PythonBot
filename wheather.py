import pyowm

owm = pyowm.OWM('e3228b63f0806d1c44e84f5a11d82640', language = "ru")
place = input ("Enter city or country: ")
observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]
print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура в районе " + str(temp))

if temp < 10:
	print("Ochen Holodno")
elif temp:
    print("Norm pogoda")
else:
	print("Teplo")