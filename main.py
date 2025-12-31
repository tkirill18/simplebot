import telebot
import config
from telebot import types
bot=telebot.TeleBot(token=config.token)
# обработка кнопки старт
@bot.message_handler(commands=['start'])
def wellcome(m):
# ответ на сообщение 
   bot.send_message('Привет я бот')

# Работа по модели long-polling.
bot.polling()
