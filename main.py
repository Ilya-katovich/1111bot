import requests
from datetime import datetime
import telebot
from auth_data import token
import webbrowser

def get_data():
    req = webbrowser.open_new_tab('https://myfin.by/api/currency/minsk')
    print(req)


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["HI"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello Boss!")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "many":
            try:
                req = webbrowser.open_new_tab('https://myfin.by/api/currency/minsk')


            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "AAAAAAAAAAA"
                )
        else:
            bot.send_message(message.chat.id, "Whaaat?Boss!")

    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)
