import os
import telebot
import parser
import bs4

#main variables
token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду советовать фильмы')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - ищу фильмы.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "шкаф":
        bot.send_message(chat_id, 'ШКАфффф ооо дааа!!!')
    elif text == "зеркало":
        bot.send_message(chat_id, 'ОООгромное ЗЕРКАЛО!!!')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')

bot.polling()
