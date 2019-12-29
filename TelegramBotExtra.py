# python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ValidationService as vs

updater = Updater(token='1033893928:AAGs8uBN1TS_esOodN3exlbaLu-rJJVreoE', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to CreditCard Validation Bot Service")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please Insert Credit Card Number")

# context.bot.send_message(chat_id=update.effective_chat.id, text="")

def replay(update, context):

    card = update.message.text
    """Here you need to add the conditions statements """
    return


updater.start_polling()
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text, replay)
dispatcher.add_handler(message_handler)