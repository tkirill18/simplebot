import telebot
import config
from telebot import types
bot=telebot.TeleBot(token=config.token)
@bot.message_handler(commands=['start'])
def wellcome(m):
   bot.send_message('Привет я бот')

bot.polling()