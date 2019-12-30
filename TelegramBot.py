# python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ValidationService as vs

updater = Updater(token='TokenHere', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to CreditCard Validation Bot Service")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please Insert Credit Card Number")

# context.bot.send_message(chat_id=update.effective_chat.id, text="")

def replay(update, context):

    card = update.message.text
    if vs.isANumber(card):
        if vs.creditCardLength(card):
            if vs.credidCardNumberSum(card):
                if vs.prefixDigit(card)[0]:
                    # Message here
                    return
                else:
                    # Message here
                    return
            else:
                # Message here
                return
        else:
            #Message here
            return
    else:
        # Message here
        return


updater.start_polling()
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text, replay)
dispatcher.add_handler(message_handler)
