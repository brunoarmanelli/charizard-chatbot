from __app__.chatbot.base import *

def get_intent(text):
    query_url = config.luis_url + text

    try:
        r = requests.get(url = query_url)
        data = r.json()

        return str(data['topScoringIntent']['intent'])
    except: 
        return None