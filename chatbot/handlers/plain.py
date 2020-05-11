from __app__.chatbot.base import *

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    analytics.handled(message.chat.id, message.text)
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, 'Sua intent foi ' + cognitive.get_intent(message.text))