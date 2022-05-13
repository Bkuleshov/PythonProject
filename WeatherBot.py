import telebot
import requests

botToken = "5341494742:AAGTtkY2hNDVTnsTSHPDmZsY_t4aUTA31eo"
apiKey = "bccc256b25008606026828a90cadfbf2"
bot = telebot.TeleBot(botToken)

@bot.message_handler(commands=['weather'])
def current_weather(message):
    cityName = message.text[9:]
    data = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': cityName, 'units': 'metric', 'APPID': apiKey}).json()
    if str(data['cod']) != '200':
        bot.send_message(message.chat.id, 'Error: no such city found')
        return
    weather = 'Current weather in ' + cityName + ': \n'
    weather += 'Temperature: ' + str(data['main']['temp']) + ' \n'
    weather += 'Cloudiness: ' + str(data['weather'][0]['main']) + ' \n'
    weather += 'Humidity: ' + str(data['main']['humidity']) + ' \n'
    weather += 'Wind speed: ' + str(data['wind']['speed']) + ' \n'
    bot.send_message(message.chat.id, weather)
    

@bot.message_handler(commands=['forecast'])
def five_days_weather(message):
    cityName = message.text[10:]
    data = requests.get("http://api.openweathermap.org/data/2.5/forecast", params = {'q': cityName, 'units': 'metric', 'APPID': apiKey}).json()
    if str(data['cod']) != '200':
        bot.send_message(message.chat.id, 'Error: no such city found')
        return
    forecast = 'Weather forecast for ' + cityName + ': \n'
    for i in range(0, len(data['list'])):
        forecast += 'Date: ' + str(data['list'][i]['dt_txt']) + ' \n'
        forecast += 'Temperature: ' + str(data['list'][i]['main']['temp']) + ' \n'
        forecast += 'Cloudiness: ' + str(data['list'][i]['weather'][0]['main']) + ' \n'
        forecast += 'Humidity: ' + str(data['list'][i]['main']['humidity']) + ' \n'
        forecast += 'Wind speed: ' + str(data['list'][i]['wind']['speed']) + ' \n'
    bot.send_message(message.chat.id, forecast)

@bot.message_handler(commands=['coordinates'])
def get_coordinates(message):
    cityName = message.text[13:]
    data = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': cityName, 'units': 'metric', 'APPID': apiKey}).json()
    if str(data['cod']) != '200':
        bot.send_message(message.chat.id, 'Error: no such city found')
        return
    coordinates = 'Coorditates of ' + cityName + ' are: \n'
    coordinates += 'Latitude: ' + str(data['coord']['lat']) + ' \n'
    coordinates += 'Longitude: ' + str(data['coord']['lon']) + ' \n'
    bot.send_message(message.chat.id, coordinates)

@bot.message_handler(commands=['timezone'])
def get_timezone(message):
    cityName = message.text[10:]
    data = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': cityName, 'units': 'metric', 'APPID': apiKey}).json()
    if str(data['cod']) != '200':
        bot.send_message(message.chat.id, 'Error: no such city found')
        return
    difference = int(data['timezone']) // 3600
    timezone = 'Timezone of ' + cityName + ': UTC' + str(difference) 
    bot.send_message(message.chat.id, timezone)

bot.polling()
