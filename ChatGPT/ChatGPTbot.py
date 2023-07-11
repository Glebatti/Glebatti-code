# 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
import openai, telebot

KEY = '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'
telegram_key = '6300397021:AAH0DXaLGmzfrgGWC5j2swMqyWQZGxc9PHw'
openai.api_key = KEY

bot = telebot.TeleBot(telegram_key)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, я твой ChatGPT бот. Готов тебе помочь!')



@bot.message_handler(content_types=['text'])
def generate_response(message):
    reply = ''
    response = openai.Completion.create(
        prompt=message.text,
        engine='text-davinci-003',
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = 'Ой, что то не так'
    bot.send_message(message.chat.id, reply)


# res = generate_response('Привет,как у тебя дела? Какая погода в Лондоне?')
# print(res)

bot.polling(none_stop=True)
