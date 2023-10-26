
from telegram import KeyboardButton,ReplyKeyboardMarkup,Update,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardRemove
def contact_send():
    contact_send=[
        [KeyboardButton('SEND CONTACT',request_contact=True)]
    ]
    return ReplyKeyboardMarkup(contact_send,resize_keyboard=True)

def fastfood_all_types():
    fastfood_buttons=[
        [InlineKeyboardButton('Lavash',callback_data='lavsh'),InlineKeyboardButton('Burger',callback_data='burger')],
        [InlineKeyboardButton('Hoddog',callback_data='hoddog'),InlineKeyboardButton('Dessert',callback_data='dessert')],
        [InlineKeyboardButton('Pizza',callback_data='pizza'),InlineKeyboardButton('Xaggi',callback_data='xagi')],
        [InlineKeyboardButton('Gamburger',callback_data='gamburger'),InlineKeyboardButton('Non',callback_data='non')],
        [InlineKeyboardButton('Order history', callback_data='history')],
        [InlineKeyboardButton('Add to Cart',callback_data='eddtocart')],
    ]
    return InlineKeyboardMarkup(fastfood_buttons)

def lavash_all_types():
    lavash_buttons=[
        [InlineKeyboardButton('Lavash cheese', callback_data='lavash cheese'), InlineKeyboardButton('Lavash mini', callback_data='lavash mini')],
        [InlineKeyboardButton('Lavash max', callback_data='lavsh max'), InlineKeyboardButton('Lavash eco', callback_data='lavash eco')],
        [InlineKeyboardButton('⬅️Back', callback_data='back')],
    ]
    return InlineKeyboardMarkup(lavash_buttons)

def back_button():
    back_buttons=[
        [InlineKeyboardButton('Cancle',callback_data='cancle'),InlineKeyboardButton('Add To Cart',callback_data='addtocart')],
        [InlineKeyboardButton('Back',callback_data='back1')]
    ]
    return InlineKeyboardMarkup(back_buttons)
