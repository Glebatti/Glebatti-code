import telebot
import sqlite3
from aiogram import types, bot, Dispatcher
import webbrowser
from Handlers_telegram_bot.venv.create_bot import Bot, dp


# @bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт 😀')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить предыдущее сообщение')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    #file = open('./Photo.jpg', 'rb')
    #dp.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    # bot.register_next_step_handler(message, on_click)


# @bot.message_handler(commands=['registr'])
def registr(message):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    dp.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
    dp.register_next_step_handler(message, user_name)


# @bot.message_handler(commands=['registr'])
def user_name(message):
    global name
    name = message.text.strip()
    dp.send_message(message.chat.id, 'Введите пароль')
    dp.register_next_step_handler(message, user_pass)


# @bot.message_handler(commands=['registr'])
def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    dp.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)


# @bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')


# @bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    message.from_user.last_name = "GOD"
    dp.send_message(message.chat.id, f'Привет, {message.from_user.first_name}  {message.from_user.last_name}')


# @bot.message_handler(commands=['help'])
def main(message):
    message.from_user.last_name = "GOD"
    dp.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(registr, commands=['registr'])
    dp.register_message_handler(user_name, commands=['registr'])
    dp.register_message_handler(user_pass, commands=['registr'])
    dp.register_message_handler(site, commands=['site', 'website'])
    dp.register_message_handler(main, commands=['start', 'main', 'hello'])
    dp.register_message_handler(main, commands=['help'])
