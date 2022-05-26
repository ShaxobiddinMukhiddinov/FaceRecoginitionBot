from telegram.ext import Updater, CommandHandler

def start_command(update, context):
    print(update.message.text)
    print(context.bot)
    print(update.message.from_user.id)
    update.message.reply_text(text='Siz /start berdingiz!')
    context.bot.send_message(chat_id='103587268', text='Ikkinchi xabar!')


updater = Updater(token="1954972158:AAGksFgEIsJWyeo2yM6YUjVfQgnS4DQvhZE")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))

updater.start_polling()
updater.idle()

