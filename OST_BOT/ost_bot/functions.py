
from buttons import *

def command_contact_send(update,context):
    update.message.reply_text('you want to send your contact to ost_test_bot', reply_markup=contact_send())
    return 'message_fastfood'


def message_fastfood(update,context):
    contact=update.effective_message.contact

    update.message.reply_text('Botimizdan foydalanishingiz mumkin',reply_markup=ReplyKeyboardRemove())
    update.message.reply_photo(photo=open('images/main.jpg','rb'),caption="Yetkazib berish bo'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.")
    update.message.reply_text('Buyirmani birga joylaymizmi❓ 😄😃😀',reply_markup=fastfood_all_types())
    return 'callbackquery_lavash_all'

def callbackquery_lavash_all(update,context):
    query=update.callback_query
    callback=query.data
    print(callback)
    query.message.delete()
    if callback=='lavsh':
        query.message.reply_photo(photo=open('images/lavash.jpg','rb'),caption=f'Bo\'lim: 🌯 {callback}',reply_markup=lavash_all_types())


    return 'callbackquery_lavash_one'


def callbackquery_lavash_one(update,context):
    query=update.callback_query
    callback=query.data
    print(callback)
    query.message.delete()
    if callback=='back':
        query.message.reply_text('Buyirmani birga joylaymizmi❓ 😄😃😀',reply_markup=fastfood_all_types())
        return 'callbackquery_lavash_all'

    query.message.reply_text(f"""Siz tanladingiz: {callback} 
        
Narx: 22000 so'm
-----
Iltimos, kerakli bo’lgan miqdorni kiriting!‍ https://cdn.delever.uz/delever/a4350a0c-cef4-408a-8433-3d462f4390f0""",reply_markup=back_button())
    return 'callbackquery_lavash_one'





