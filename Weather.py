import requests

def getweather():

    apikey = "8352ebdbd0ef002753e1b61f4c02256f"
    city = "Orlando"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&units=imperial&appid="+apikey

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    tempmin = json.get("main").get("temp_min")
    tempmax = json.get("main").get("temp_max")

    return {"description": description,
            "tempmin": tempmin,
            "tempmax": tempmax}

# print(json)

weather_dict = getweather()


print("Today's forecast is", weather_dict.get("description"))
print("Today's minimum temperature is", weather_dict.get("tempmin"))
print("Today's maximum temperature is", weather_dict.get("tempmax"))

temperature = int(input("What is the temperature?\n"))

if temperature > 80:
    print("It's too hot!")
    print("Stay inside.")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside.")
else:
    print("Let's go hiking!")    