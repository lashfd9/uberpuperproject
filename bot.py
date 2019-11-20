import os
import telebot
import parser

#main variables
token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)
