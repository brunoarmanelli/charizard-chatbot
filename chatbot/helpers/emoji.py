from __app__.chatbot.base import *

def remove_from_text(text):
    return emoji.get_emoji_regexp().sub(u'', text).strip('')