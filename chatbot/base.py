#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Plugins/Modules
import logging
import telebot
import time as t
from datetime import datetime, date, time, timedelta
from telebot import apihelper, types
from chatbase import Message, MessageSet, MessageTypes, InvalidMessageTypeError
import re
import requests
import emoji
import random

# Configs
from . import config as config

# Set Logger
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Init Chatbot
bot = telebot.TeleBot(config.telegram_token)

# Helpers
from .helpers import analytics as analytics
from .helpers import emoji as emojify
from .helpers import cognitive as cognitive

# Message Handlers
from .handlers import callbacks, commands, media, plain