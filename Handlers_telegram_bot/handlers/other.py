from aiogram import types, Dispatcher
import webbrowser
import sqlite3
import telebot
from Handlers_telegram_bot.venv.create_bot import Bot, dp



# @dp.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     conn = sqlite3.connect('itproger.sql')
#     cur = conn.cursor()
#
#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#
#     info = ''
#     for el in users:
#         info += f'Имя: {el[1]}, пароль: {el[2]}\n'
#     cur.close()
#     conn.close()
#
#     dp.send_message(callback.message.chat.id, info)


@dp.message_handler()
def info(message):
    message.from_user.last_name = "GOD"
    if message.text.lower() == 'привет':
        dp.send_message(message.chat.id, f'Привет, {message.from_user.first_name}  {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        dp.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text == 'Перейти на сайт 😀':
        dp.send_message(message.chat.id, 'Website is open')
        webbrowser.open('https://itproger.com')
    elif message.text == 'Удалить предыдущее сообщение':
        dp.send_message(message.chat.id, 'Delete')
        dp.delete_message(message.chat.id, message.message_id - 1)
    elif message.text == 'Изменить текст':
        dp.send_message(message.chat.id, 'Edit')
        dp.delete_message(message.chat.id, message.message_id)

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(info)