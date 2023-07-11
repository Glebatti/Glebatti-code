import telebot
import sqlite3
import webbrowser
from telebot import types
from create_bot import dp
from Handlers_telegram_bot.handlers import client, admin, other
from aiogram.utils import executor

client.register_handlers_client(dp)
other.register_handlers_other(dp)














executor.start_polling(dp)



#def on_click(message):
    #if message.text == 'Перейти на сайт':
        #bot.send_message(message.chat.id, 'Website is open')
    #elif message.text == 'Удалить фото':
        #bot.send_message(message.chat.id, 'Delete')




# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)






