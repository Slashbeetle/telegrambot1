import os
from Keepalive import keep_alive

from telegram import*
from telegram.ext import*

my_secret = os.environ['TOKEN']

#bot = Bot("1779113707:AAH5b50y7Qo-aRcFmq094KiQ_VEJJNERcrw")
bot = Bot(my_secret)

print(bot.get_me())
updater = Updater(my_secret,use_context="true")

dispatcher= updater.dispatcher


def start(update:Update,context:CallbackContext):
  bot.send_message(
      chat_id=update.effective_chat.id,
      text= "Hi there , welcome to Spam bot........hope you would love my services...",
  )

def spamfn0(update:Update,context:CallbackContext):
  bot.send_message(
      chat_id=update.effective_chat.id,
      text= "hi hello world",
  )


def spamfn1(update:Update,context:CallbackContext):
  bot.send_message(
      chat_id=update.effective_chat.id,
      text= "hi hello world welcome",
  )


start_value= CommandHandler('spam',spamfn0)
dispatcher.add_handler(start_value)
updater.start_polling()

start_value= CommandHandler('spam1',spamfn1)
dispatcher.add_handler(start_value)
updater.start_polling()

start_value= CommandHandler('start',start)
dispatcher.add_handler(start_value)
updater.start_polling()





keep_alive()
token = os.environ.get("token")
#bot.run(token)
