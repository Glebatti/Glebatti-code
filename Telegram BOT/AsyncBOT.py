from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
bot = Bot('6095178864:AAEQ5gGH7LZ79CGTejQoXjITwF5ULJboWe8')
dp = Dispatcher(bot)

#
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://itproger.com')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. + Email: {res["email"]}. Phone: {res["phone"]}')




@dp.message_handler(commands=['hello'])  # commands=['start']
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    await message.reply('Hello')
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)





@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://itproger.com')) #https://itproger.com/telegram.html(не работает нужный адрес)
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)

executor.start_polling(dp)
