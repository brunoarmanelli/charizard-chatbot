#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from .base import *
import azure.functions as func

# Set bot pooling for development. Use a different key for staging to avoid disabling production webhook.
if(config.env and config.env == 'Development'):
    bot.set_webhook(url='')
    bot.polling(none_stop=True)

# HTTP Listner
def main(req: func.HttpRequest) -> func.HttpResponse:
    # Set webhook only once to avoid "error 429 too many request" or use time.sleep(1).
    bot.set_webhook(url=config.webhook_url)

    request_body_dict = req.get_json()
    update = telebot.types.Update.de_json(request_body_dict)
    bot.process_new_messages([update.message])
    return func.HttpResponse(body='', status_code=200)
