from telegram.ext import Updater, CommandHandler

import requests

import re

contents = requests.get('https://random.dog/woof.json').json()

{"url":"https://random.dog/62d87d11-bcdb-410f-8aee-324fe07f0c70.mp4"}

image_url = contents['url']

def get_url():

    contents = requests.get('https://random.dog/woof.json').json()    

    url = contents['url']

    return url

url = get_url()

chat_id = update.message.chat_id

bot.send_photo(chat_id=chat_id, photo=url)

def bop(bot, update):

    url = get_url()

    chat_id = update.message.chat_id

    bot.send_photo(chat_id=chat_id, photo=url)

    

    def main():

    updater = Updater('1338444225:AAH2Qk88SHpMRpUVPls8K1YBQEvuIkgKFHs')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bop',bop))

    updater.start_polling()

    updater.idle()

    

if __name__ == '__main__':

    main()
