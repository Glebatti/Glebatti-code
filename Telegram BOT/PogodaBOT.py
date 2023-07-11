import telebot
import requests
import json
import sqlite3
import webbrowser
from telebot import types

bot = telebot.TeleBot('6144823642:AAEwuIyVjDf5TbCAfTkcUPGEmVxWy-8AndU')
API ='d46e2c93fafdf3d5198d143844d8c4e4'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название')



@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]

        bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}')
        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')


bot.infinity_polling()