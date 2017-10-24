
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
#from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from key import apikey
from urllib.parse import urlparse
import os, logging, datetime, json, random, time
from pymongo import MongoClient

db = 0
char_info = {}

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def load_info():
    global char_info
    global db

    client = MongoClient(str(os.environ["MONGODB_URI"]))  # connect to the server
    db = client[str(os.environ["MONGODB_DATABASE"])]  # connect to database

    char_collection = db.charinfo  # select collection

    char_info = char_collection.find_one()
    print(char_info)

    if char_info is None:
        char_info = {}


def save_info():
    global char_info
    global db

    db.charinfo.update({}, char_info, upsert=True)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Hey!")


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Just ask @Epowerj. This bot currently uses a dev build.')


def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='Pong')


def time(bot, update):
    bot.sendMessage(update.message.chat_id, text=str(datetime.datetime.now()))


def chatinfo(bot, update):
    bot.sendMessage(update.message.chat_id, text="chat_id is "+str(update.message.chat_id))
    bot.sendMessage(update.message.chat_id, text="user id is "+str(update.message.from_user.id))


def error(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))


def parse(bot, update):
    #print(str(update.channel_post.chat_id))
    print("file: " + str(update.message.document.file_id))
    print("Message from " + update.message.from_user.first_name + "(" + str(update.message.from_user.id) + "): " +
          update.message.text + " (" + str(update.message.message_id) + ")")


def info(bot, update): #TODO add automatic indexing an inline buttons
    global char_info

    commandtext = update.message.text.split(' ')

    if len(commandtext) >= 2:
        commandtext = commandtext[1].lower()

        if commandtext in char_info:
            bot.sendMessage(update.message.chat_id, text=char_info[commandtext])
        else:
            bot.sendMessage(update.message.chat_id, text="No info found on '"+commandtext+"'")
    else:
        bot.sendMessage(update.message.chat_id, text="Usage: /info <topic>")


def setinfo(bot, update):
    global char_info

    commandtext = update.message.text.split(' ', 2)

    char_info[commandtext[1].lower()] = commandtext[2]

    save_info()

    bot.sendMessage(update.message.chat_id, text="Info saved")


def main():
    global char_info

    load_info()
    print(char_info)

    TOKEN = apikey
    PORT = int(os.environ.get('PORT', '5000'))
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.setWebhook("https://" + str(os.environ.get("APPNAME")) + ".herokuapp.com/" + TOKEN)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("chatinfo", chatinfo))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("setinfo", setinfo))

    dp.add_handler(MessageHandler(Filters.text, parse))

    dp.add_error_handler(error)

    updater.idle()


if __name__ == '__main__':
    main()
