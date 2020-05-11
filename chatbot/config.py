import os

# Bot Env
env = os.environ['AZURE_FUNCTIONS_ENVIRONMENT']

# Bot Setting
bot_name = 'Charizard Bot'

# Telegram
telegram_token = os.environ['TelegramBotKey']

# Azure Functions URL
webhook_url = os.environ['WebHookAddress']

# Chatbase
chatbase_key = os.environ['ChatbaseKey']
chatbase_platform = 'Telegram'
chatbase_version = os.environ['ChatbaseVersion']

# LUIS
luis_url = os.environ['LuisUrl']