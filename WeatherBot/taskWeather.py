import telebot
import requests
bot = telebot.TeleBot('ТОКЕН я свой убрал')
start_txt = 'Привет! Назови город.'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')
def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "units":"metric",
        "lang":"ru",
        "appid":"79d1ca96933b0328e1c7e3e7a26cb347"
    }
    weather_data = requests.get(url, params=params).json()
    return weather_data
if __name__ == '__main__':
    while True:
        @bot.message_handler(content_types=['text'])
        def weather(message):
            city = message.text
            weather_data = get_weather(city)
            temperature = round(weather_data['main']['temp'])
            temperature_feels = round(weather_data['main']['feels_like'])
            w_now = 'В городе ' + city + ' ' + str(temperature) + ' °C'
            w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
            bot.send_message(message.from_user.id, w_now)
            bot.send_message(message.from_user.id, w_feels)
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print('Исключение:', e)