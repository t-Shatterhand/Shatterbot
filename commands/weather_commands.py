import tokens
import requests


def getWeather(update, context):
    if len(update.message.text.split()) == 1:
        update.message.reply_text("Please, enter the city after /getWeather")
    else:
        city = update.message.text.split(' ', 1)[1]
        city_url = tokens.base_url + "appid=" + tokens.api_key + "&q=" + city
        response = requests.get(city_url)
        site_responded = response.json()
        if site_responded["cod"] != "404":
            searched_city = site_responded["main"]
            current_temperature = searched_city["temp"]
            celsius_temperature = round((current_temperature - 270), 3)
            fahrenheit_temperature = round((celsius_temperature * 1.8 + 32), 3)
            current_pressure = searched_city["pressure"]
            current_humidity = searched_city["humidity"]
            searched_weather = site_responded["weather"]
            weather_description = searched_weather[0]["description"]
            return_message = ("Temperature (in celsius unit) = " +
                              str(celsius_temperature) +
                              "\nTemperature (in fahrenheit unit) = " +
                              str(fahrenheit_temperature) +
                              "\nAtmospheric pressure (in hPa unit) = " +
                              str(current_pressure) +
                              "\nHumidity (in percentage) = " +
                              str(current_humidity) +
                              "\nDescription = " +
                              str(weather_description))
            update.message.reply_text(return_message)
        else:
            update.message.reply_text("City not found. Please check your query and try again")
