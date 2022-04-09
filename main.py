from tokenize import Token
import telegram.ext
import requests, json

#pip install python-telegram-bot
#pip install requests

with open('token.txt', 'r') as f:
    token = f.read()

class WeatherBor():
    def __init__(self) -> None:
        updater = telegram.ext.Updater(token, use_context=True)
        disp = updater.dispatchers

        disp.add_handler(telegram.ext.CommandHandler("start", self.start))
        disp.add_handler(telegram.ext.CommandHandler("getweather", self.getcity))
        disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, self.handle_city))

        updater.start_polling()
        updater.idle()

    def start(self, update, context):
        update.message.reply_text("""
        Hello and welcome to WEATHER BOT ;)
        PLEASE ENTER YOUR CITY NAME -->
        """)

    def getcity(self, update, context):
        update.message.reply_text("please enter your city name : ")

    def handle_city(self, update, context):
        weather = self.real_weather(update.message.text)
        update.message.reply_text(weather)

    def real_weather(self, CITY):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        #enter your weather api here 
        API_KEY = "X1X1X1X1X1X1X1X1X1X1X1X1X1X1X1X1X1X"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']
            return f"{CITY:-^30}\nTemperature: {round(int(temperature))} C°\nHumidity: {humidity} %\nPressure: {pressure} mb\nWeather Report: {report[0]['description']}"
        else:
            # showing the error message
            return "please enter a valid city name : "



WeatherBor()