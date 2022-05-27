from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

ADMIN_ID = 1035687268
TOKEN = " "


def start_command(update, context):
    # context.bot.send_message(chat_id="103587268",text='Keyingi xabar!')
    update.message.reply_text(text="Sizga /start tugmasi yoqib qolganmi?")


def show_menu(update, context):
    buttons = [
        [KeyboardButton(text="Send Message", request_contact=True),
         KeyboardButton(text="Send Location", request_location=True)],
        [KeyboardButton(text="Main Menu"), KeyboardButton(text="Menu")]
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )


def message_handler(update, context):
    message = update.message.text
    update.message.reply_text(text=f"Sizning ma'lumotingz '{message}'")


def contacts_handler(update, context):
    phone_number = update.message.contact.phone_number
    update.message.reply_text(text=f"Sizning nomeringiz : '{phone_number}'")
    context.bot.send_message(chat_id=ADMIN_ID, text=f"Yani foydalanuvchi va raqami: '{phone_number}'")


def location_handler(update, context):
    location = update.message.location
    # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
    context.bot.send_location(chat_id=ADMIN_ID, text=f" Sizga joylashuv o'rnini ulashdi!", latitude=location.latitude, longitude=location.longitude)


def main():
    updater = Updater(token="1954972158:AAGksFgEIsJWyeo2yM6YUjVfQgnS4DQvhZE")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contacts_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
