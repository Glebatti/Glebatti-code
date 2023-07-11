import telebot
import sqlite3
import webbrowser
from telebot import types

bot = telebot.TeleBot('6163108959:AAGC5h-75Ne4T6v-lNDoTmj-lMs8KQGTkGE')
name = ''



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт 😀')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить предыдущее сообщение')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./Photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    #bot.register_next_step_handler(message, on_click)


#def on_click(message):
    #if message.text == 'Перейти на сайт':
        #bot.send_message(message.chat.id, 'Website is open')
    #elif message.text == 'Удалить фото':
        #bot.send_message(message.chat.id, 'Delete')


@bot.message_handler(commands=['registr'])
def registr(message):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)


@bot.message_handler(commands=['registr'])
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

@bot.message_handler(commands=['registr'])
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
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)


# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(callback.message.chat.id, info)




@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    message.from_user.last_name = "GOD"
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}  {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    message.from_user.last_name = "GOD"
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    message.from_user.last_name = "GOD"
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}  {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text == 'Перейти на сайт 😀':
        bot.send_message(message.chat.id, 'Website is open')
        webbrowser.open('https://itproger.com')
    elif message.text == 'Удалить предыдущее сообщение':
        bot.send_message(message.chat.id, 'Delete')
        bot.delete_message(message.chat.id, message.message_id - 1)
    elif message.text == 'Изменить текст':
        bot.send_message(message.chat.id, 'Edit')
        bot.delete_message(message.chat.id, message.message_id)




bot.infinity_polling()
# bot.polling(none_stop=True)
