import constants as keys
from telegram.ext import *
import responses as R
i=0
print("bot started....")

def start_command(update, context):
    update.message.reply_text('type sth to start')

def help_command(update, context):
    update.message.reply_text('nothing to help')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)
def handle_file(update, context):
    file = 
def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.set_webhook(bot138113821624941160:AAFf5LSyMfnATrWdZ8ANaJmXSWFVXuUfyqY)
    updater.idle()

main()
