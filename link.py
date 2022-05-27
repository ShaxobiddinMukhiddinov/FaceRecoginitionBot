from telegram.ext import Updater, CommandHandler


def start_command(update, context):
    # update.message.reply_text(text='Siz /start berdingiz!')
    context.bot.send_message(chat_id='1035687268', text='Ikkinchi xabar /start!')


updater = Updater(token="1954972158:AAGksFgEIsJWyeo2yM6YUjVfQgnS4DQvhZE")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))

updater.start_polling()
updater.idle()

