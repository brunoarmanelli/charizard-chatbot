from __app__.chatbot.base import *

@bot.message_handler(content_types=['photo'])
def handle_photo_files(message):
    if message.chat.type == "private" and not customer.banned(message.chat.id):
        print(message.json)
        bot.send_message(message.chat.id, 'Não posso interpretar imagens.')