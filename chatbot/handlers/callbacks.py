from __app__.chatbot.base import *

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    print(call.data)