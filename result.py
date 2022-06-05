import face_recognition
import numpy as np
import json
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, InputMediaPhoto

ADMIN_ID = "ID"
token = 'Token'


def start_func(update, context):  # start funksiyasi-botni ishga tushdi;

    # Botga mavjud buyruqlarni qo'shish va / orqali userga chiqarish
    command_list = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="menu", description="Menu ro'yxati"),
        BotCommand(command="info", description="Bot haqida ma'lumot"),
        BotCommand(command="settings", description="Bot sozlamalari"),
    ]
    context.bot.set_my_commands(commands=command_list)
    global buttons
    buttons = [
        [InlineKeyboardButton(text='Send Photo', callback_data="send_photo"),
         InlineKeyboardButton(text="Change Photo", callback_data="change_photo")],
        [InlineKeyboardButton(text="Send Media Group", callback_data="send_media")]

    ]
    # Botga rasm joylash, o'zgartirish va bir vaqtda bir nechata rasm jo'natish

    update.message.reply_photo(
        photo='https://picsum.photos/400/200',
        caption=f"Hello, {update.message.from_user.first_name} 🖐🖐🖐 !!!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def inline_handler(update, context):
    # Inline button ishga tushganda bajaradigan vazifalar;
    query = update.callback_query
    global buttons

    if query.data == 'send_photo':
        query.message.reply_photo(
            photo=f"https://picsum.photos/id/{random.randint(1, 100)}/400/200",
            caption='New photo',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif query.data == 'change_photo':
        query.message.edit_media(
            media=InputMediaPhoto(media=f"https://picsum.photos/id/{random.randint(1, 100)}/400/200"))
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == 'send_media':
        query.message.reply_media_group(
            media=[
                # InputMediaPhoto(media=open("rasmlar/Jeki ch.jpg", "rb")),
                InputMediaPhoto(media=open("Apps/new_photo.jpg", "rb")),
                InputMediaPhoto(media=f"https://picsum.photos/id/{random.randint(1, 100)}/400/200"),
                InputMediaPhoto(media=f"https://picsum.photos/id/{random.randint(45, 100)}/400/200")
            ]
        )


def message_handler(update, context):
    # Botga kelayotgan xabarlarni o'qib qaytarib beradi;
    message = update.message.text
    update.message.reply_text(text=f"Sizning ma'lumotingz '{message}'")


def photo_handler(update, context):
    # Botga media fayllar tashlnganida uni yuklab olish;
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download('Apps/new_photo.jpg')

    with open("encode.json") as json_file:
        data = json.load(json_file)

    known_face_encodings = [np.asarray(i['encoding']) for i in data]
    # face_name = [f" Astrum talabasi\nYo'nalishi: {i['dir']}\nIsm Sharifi: {i['name']}" for i in data]
    face_name = [f" Tanishing: {i['name']} \n {i['dir']}" for i in data]

    unknown = face_recognition.load_image_file('Apps/new_photo.jpg')
    unknown_encoding = face_recognition.face_encodings(unknown)[0]

    result = face_recognition.api.compare_faces(known_face_encodings, unknown_encoding, tolerance=0.5)

    if True not in result:update.message.reply_text(text="Afsus topilmadi!!!\nUshbu ma'lumotlari meni bazamda mavjud emas!")
    for idx, i in enumerate(result):
        if i:
            update.message.reply_text(f"{face_name[idx]}")


def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
