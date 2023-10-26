
from telegram.ext import Updater,ConversationHandler,CommandHandler,MessageHandler,Filters,CallbackQueryHandler
from functions import *
from telegram import ReplyKeyboardRemove

updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')

conv_handler=ConversationHandler(
    entry_points=[
        CommandHandler('start',command_contact_send)
    ],
    states={
        'message_fastfood':[
            MessageHandler(Filters.contact,message_fastfood)
        ],

        'callbackquery_lavash_all':[
            CallbackQueryHandler(callbackquery_lavash_all)
        ],
        'callbackquery_lavash_one':[
            CallbackQueryHandler(callbackquery_lavash_one)

        ]

    },

    fallbacks=[
        CommandHandler('start',command_contact_send)
    ],
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

