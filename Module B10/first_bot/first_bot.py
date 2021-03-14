import telebot

TOKEN = "893005100:AAE-jeed2SLHp75uud6oPJZZWv4Yt7M8m-Y"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, "You have very beautiful voice")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Welcome {message.chat.username}")


@bot.message_handler(content_types=['photo'])
def handle_mem(message: telebot.types.Message):
    bot.reply_to(message, "Nice mem, bro")


bot.polling(none_stop=True)
