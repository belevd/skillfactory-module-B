import telebot
from config import TOKEN
from constants import CURRENCIES
from convert import convert

bot = telebot.TeleBot(TOKEN)

intro_text = '''
Привет! Этот бот умеет конвертировать валюты.\n
Введи /values и посмотри, какие валюты он поддерживает\n
Для конвертации отправь сообщение следующего вида:\n
<из какой валюты конвертируем> <в какую валюту конвертируем> <кол-во первой валюты>
Удачного использования!
'''


@bot.message_handler(commands=['start', 'help'])
def introduce(message: telebot.types.Message):
    bot.reply_to(message, intro_text)


@bot.message_handler(commands=['values'])
def print_values(message: telebot.types.Message):
    text = 'На данный момент доступны следующие валюты: '
    for key in CURRENCIES.keys():
        text += f'\n{key}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def handle_text(message: telebot.types.Message):
    result = convert(message.text)
    bot.reply_to(message, result)


if __name__ == '__main__':
    bot.polling(none_stop=True)


