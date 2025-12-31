import telebot
import config
from telebot import types
bot=telebot.TeleBot(token=config.token)
# обработка кнопки старт
@bot.message_handler(commands=['start'])
def wellcome(m):
   # ответ на сообщение 
   bot.send_message(text='Привет я бот',chat_id=m.chat.id)

# Работа по модели long-polling.
bot.polling()
