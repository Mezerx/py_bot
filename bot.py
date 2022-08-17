import config
import telebot
from codbase import base
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    try:
        bot.send_message(message.chat.id, base[message.text])
    except:
        KeyError


bot.polling(none_stop=True)