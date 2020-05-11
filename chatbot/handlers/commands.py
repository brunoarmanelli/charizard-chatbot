from __app__.chatbot.base import *

@bot.message_handler(commands=['start'])
def start(message):
    analytics.handled_intent(message.chat.id, 'start', message.text)
    bot.reply_to(message, 'Olá, ' + message.from_user.first_name + '!')