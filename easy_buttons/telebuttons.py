#  /////  OUTLINE_BUTTONS without function /////////////////////////////////////////////////////////
# from telegram import Update,ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# outline_buttons=[
#     ['Enter']
#
# ]
#
# def command_outline_buttons(update,context):
#     update.message.reply_text('Outline buttons',reply_markup=ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True))
#
# updater.dispatcher.add_handler(CommandHandler('start',command_outline_buttons))
#
# updater.start_polling()
# updater.idle()

#  ////////////// OUTLINE_BUTTONS  with Function /////////////////////////////////////////////////////////

# from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
# from telegram.ext import Updater, CommandHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def outline_keyboard_buttons():
#     outline_buttons=[
#         [KeyboardButton('Enter')]
#     ]
#     return ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True)
#
# def command_outline_buttons(update,context):
#     update.message.reply_text('Outline buttons', reply_markup=outline_keyboard_buttons())
#
# updater.dispatcher.add_handler(CommandHandler('start',command_outline_buttons))
#
# updater.start_polling()
# updater.idle()

#  /////////////   INLINE_BUTTONS without function    ///////////////////////////////////////////////////////
# from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# fastfood_buttons=[
#     [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#     [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#     [InlineKeyboardButton('Back',callback_data='back')]
# ]
#
# def command_inline_buttons(update, context):
#     update.message.reply_text('Inline button',reply_markup=InlineKeyboardMarkup(fastfood_buttons))
#
# updater.dispatcher.add_handler(CommandHandler('start',command_inline_buttons))
#
# updater.start_polling()
# updater.idle()

#   /////////////   INLINE_BUTTONS with function    ///////////////////////////////////////////////////////
# from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def inline_buttons_fastfood():
#     fastfood_buttons=[
#     [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#     [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#     [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(fastfood_buttons)
#
# def command_inline_buttons(update, context):
#     update.message.reply_text('Inline button',reply_markup=inline_buttons_fastfood())
#
# updater.dispatcher.add_handler(CommandHandler('start',command_inline_buttons))
#
# updater.start_polling()
# updater.idle()

#  /////////////////////  OUTLINE and INLINE BUTTONs without function dan INLINE_BUTTON hosil qilish  ///////////////////////////////////////////
# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# outline_buttons=[
#     ['Enter']
# ]
#
# inline_buttons=[
#     [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#     [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#     [InlineKeyboardButton('Back',callback_data='back')]
# ]
#
# def command_outline_buttons(update,context):
#     update.message.reply_text('Outline buttons',reply_markup=ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True))
#
# def message_inline_buttons(update,context):
#     update.message.reply_text('Outline button bosilganda inline button hosil bulishi',reply_markup=InlineKeyboardMarkup(inline_buttons))
#
#
# updater.dispatcher.add_handler(CommandHandler('start', command_outline_buttons))
#
# updater.dispatcher.add_handler(MessageHandler(Filters.regex('^('+ 'Enter' +')$'),message_inline_buttons))
#
# updater.start_polling()
# updater.idle()

# /////////////////////  OUTLINE and INLINE BUTTONs with function dan INLINE_BUTTON hosil qilish  //////////////////
# ///// add_handler(p), p=CommandHandler, CommandHandler(p1,p2), p1='start', p2=function
# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,KeyboardButton,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def outline_keyboard_buttons():
#     outline_buttons=[
#         [KeyboardButton('Enter')]
#     ]
#     return ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True)
#
# def inline_buttons_fastfood():
#     fastfood_buttons=[
#     [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#     [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#     [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(fastfood_buttons)
#
# def command_outline_buttons(update,context):
#     update.message.reply_text('Outline buttons',reply_markup=outline_keyboard_buttons())
#
# def message_inline_buttons(update,context):
#     update.message.reply_text('Outline button bosilganda inline button hosil bulishi',reply_markup=inline_buttons_fastfood())
#
#
# updater.dispatcher.add_handler(CommandHandler('start', command_outline_buttons))
#
# updater.dispatcher.add_handler(MessageHandler(Filters.regex('^('+ 'Enter' +')$'),message_inline_buttons))
#
#
# updater.start_polling()
# updater.idle()

# /////       OUTLINE and INLINE BUTTONs with function dan INLINE_BUTTON hosil qilish    ///////////////////////////////
#  //////  ConversationHandler(p1,p2,p3), p1,p2 va p3-parametrs, p1=entry_points=[], p2=states={}, p3=fallbacks=[]    /////////

# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def outline_buttons_fastfood():
#     outline_buttons=[
#         [KeyboardButton('Enter')]
#     ]
#     return ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True)
#
# def inline_buttons_fastfood():
#     fastfood_buttons=[
#         [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#         [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#         [InlineKeyboardButton('Delete',callback_data='delete')]
#     ]
#     return InlineKeyboardMarkup(fastfood_buttons)
#
# def command_outline_buttons(update, context):
#     update.message.reply_text('Outline button with function',reply_markup=outline_buttons_fastfood())
#     return 'message_inline'
#
# def message_inline_buttons(update,context):
#     update.message.reply_text('Inline button with function',reply_markup=inline_buttons_fastfood())
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_outline_buttons)
#     ],
#     states={
#         'message_inline':[
#             MessageHandler(Filters.regex('^('+ 'Enter' +')$'),message_inline_buttons)
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',command_outline_buttons)
#     ]
# )
# updater.dispatcher.add_handler(conv_handler)
# updater.start_polling()
# updater.idle()

#  /////////////////////// INLINE BUTTONS FUNCTIONlarni bosgandagi hodisalar ///// ///////////////////////////////////////////////////////////

# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def outline_buttons_fastfood():
#     outline_buttons=[
#         [KeyboardButton('Enter')]
#     ]
#     return ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True)
#
# def inline_buttons_fastfood():
#     fastfood_buttons=[
#         [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#         [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#         [InlineKeyboardButton('Delete',callback_data='delete')]
#     ]
#     return InlineKeyboardMarkup(fastfood_buttons)
#
# # The button section
# def inline_buttons_lavash():
#     lavash_buttons=[
#         [InlineKeyboardButton('Lavash 1',callback_data='lavash1'),InlineKeyboardButton('Lavash 2 ',callback_data='lavash2')],
#         [InlineKeyboardButton('Lavash 3 ',callback_data='lavash3'),InlineKeyboardButton('Lavash 4 ',callback_data='lavash4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(lavash_buttons)
#
# def inline_buttons_burger():
#     burger_buttons=[
#         [InlineKeyboardButton('Burger 1',callback_data='burger1'),InlineKeyboardButton('Burger 2',callback_data='burger2')],
#         [InlineKeyboardButton('Burger 3',callback_data='burger3'),InlineKeyboardButton('Burger 4',callback_data='burger4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(burger_buttons)
#
# def inline_buttons_hoddog():
#     hoddog_buttons=[
#         [InlineKeyboardButton('Hoddog 1',callback_data='hoddog1'),InlineKeyboardButton('Hoddog 2',callback_data='hoddog2')],
#         [InlineKeyboardButton('Hoddog 3',callback_data='hoddog3'),InlineKeyboardButton('Hoddog 4',callback_data='hoddog4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(hoddog_buttons)
#
# def inline_buttons_cocacola():
#     cocacola_buttons=[
#         [InlineKeyboardButton('Coca cola 1',callback_data='cocacola1'),InlineKeyboardButton('Coca Cola 2',callback_data='cocacola2')],
#         [InlineKeyboardButton('Coca cola 3',callback_data='cocacola3'),InlineKeyboardButton('Coca Cola 4',callback_data='cocacola4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(cocacola_buttons)
# # The function secsion
#
# def command_start(update, context):
#     update.message.reply_text('Assalomu alaykum!',reply_markup=outline_buttons_fastfood())
#     return 'message_filters_regex'
#
# def message_filters_regex(update,context):
#     update.message.reply_text('Fastfood turlari',reply_markup=inline_buttons_fastfood())
#     return 'callbackquery_in_value'
#
# def callbackquery_in_value(update,context):
#     query=update.callback_query
#     print(query.data)
#     if query.data == 'lavash':
#         query.message.reply_html("<b>Lavash</b> turlari",reply_markup=inline_buttons_lavash())
#     elif query.data=='burger':
#         query.message.reply_html("<b>Burger</b> turlari",reply_markup=inline_buttons_burger())
#     elif query.data=='hoddog':
#         query.message.reply_html("<b>Hoddog</b> turlari",reply_markup=inline_buttons_hoddog())
#     elif query.data=='coca cola':
#         query.message.reply_html("<b>Coca Cola</b> turlari",reply_markup=inline_buttons_cocacola())
#
#     elif query.data=='back':
#         query.message.reply_text("Fastfood turlari",reply_markup=inline_buttons_fastfood())
#
# conversation_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_start)
#     ],
#     states={
#         'message_filters_regex':[
#             MessageHandler(Filters.regex('^('+ 'Enter' +')$'),message_filters_regex),
#         ],
#         'callbackquery_in_value':[
#
#             CallbackQueryHandler(callbackquery_in_value)
#         ]
#     },
#     fallbacks=[
#         CommandHandler('start',command_start)
#     ]
# )
# updater.dispatcher.add_handler(conversation_handler)
# updater.start_polling()
# updater.idle()

#   /////// reply_html(p1,p2) and reply_text(p1,p2)-functions, p1,p2-parameters, p1='text', p2=reply_markup, //////////

# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def outline_buttons_fastfood():
#     outline_buttons=[
#         [KeyboardButton('Enter')]
#     ]
#     return ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True)
#
# def inline_buttons_fastfood():
#     fastfood_buttons=[
#         [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#         [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#         [InlineKeyboardButton('Delete',callback_data='delete')]
#     ]
#     return InlineKeyboardMarkup(fastfood_buttons)
#
# # bu yerga har biriga ichki qisim inline buttons funksiyalarini yozamiz
# def inline_buttons_lavash():
#     lavash_buttons=[
#         [InlineKeyboardButton('Lavash 1',callback_data='lavash1'),InlineKeyboardButton('Lavash 2 ',callback_data='lavash2')],
#         [InlineKeyboardButton('Lavash 3 ',callback_data='lavash3'),InlineKeyboardButton('Lavash 4 ',callback_data='lavash4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(lavash_buttons)
#
# def inline_buttons_burger():
#     burger_buttons=[
#         [InlineKeyboardButton('Burger 1',callback_data='burger1'),InlineKeyboardButton('Burger 2',callback_data='burger2')],
#         [InlineKeyboardButton('Burger 3',callback_data='burger3'),InlineKeyboardButton('Burger 4',callback_data='burger4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(burger_buttons)
#
# def inline_buttons_hoddog():
#     hoddog_buttons=[
#         [InlineKeyboardButton('Hoddog 1',callback_data='hoddog1'),InlineKeyboardButton('Hoddog 2',callback_data='hoddog2')],
#         [InlineKeyboardButton('Hoddog 3',callback_data='hoddog3'),InlineKeyboardButton('Hoddog 4',callback_data='hoddog4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(hoddog_buttons)
#
# def inline_buttons_cocacola():
#     cocacola_buttons=[
#         [InlineKeyboardButton('Coca cola 1',callback_data='cocacola1'),InlineKeyboardButton('Coca Cola 2',callback_data='cocacola2')],
#         [InlineKeyboardButton('Coca cola 3',callback_data='cocacola3'),InlineKeyboardButton('Coca Cola 4',callback_data='cocacola4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(cocacola_buttons)
#
# # Function qisim
#
# def command_outline_start(update, context):
#     update.message.reply_text('Assalomu alaykum!',reply_markup=outline_buttons_fastfood())
#     return 'message_filters_regex'
#
# def message_filters_regex(update,context):
#     update.message.reply_html('<b>Fastfood</b> turlari',reply_markup=inline_buttons_fastfood())
#     return 'callbackquery_in_value'
#
#
# def callbackquery_in_value(update,context):
#     query=update.callback_query
#     print(query.data)
#     # query.message.delete()
#
#     if query.data == 'lavash':
#         query.message.reply_html("<b>Lavash</b> turlari",reply_markup=inline_buttons_lavash())
#
#     elif query.data=='burger':
#         query.message.reply_html("<b>Burger</b> turlari",reply_markup=inline_buttons_burger())
#     elif query.data=='hoddog':
#         query.message.reply_html("<b>Hoddog</b> turlari",reply_markup=inline_buttons_hoddog())
#     elif query.data=='coca cola':
#         query.message.reply_html("<b>Coca Cola</b> turlari",reply_markup=inline_buttons_cocacola())
#
#     elif query.data=='back':
#         query.message.reply_html("<b>Fastfood </b> turlari",reply_markup=inline_buttons_fastfood())
#
# conversation_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_outline_start)
#     ],
#     states={
#         'message_filters_regex':[
#             MessageHandler(Filters.regex('^('+ 'Enter' +')$'),message_filters_regex),
#         ],
#         'callbackquery_in_value':[
#
#             CallbackQueryHandler(callbackquery_in_value)
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',command_outline_start)
#     ]
# )
# updater.dispatcher.add_handler(conversation_handler)
# updater.start_polling()
# updater.idle()


#  //////////// edit_message_text(p1,p2)- function, p1='text', p2=reply_text,      /////////////////////////
# /// Updater(p)-function, p='Token',

# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
#
# def outline_buttons_fastfood():
#     outline_buttons=[
#         [KeyboardButton('Enter')]
#     ]
#     return ReplyKeyboardMarkup(outline_buttons,resize_keyboard=True)
#
# def inline_buttons_fastfood():
#     fastfood_buttons=[
#         [InlineKeyboardButton('Lavash',callback_data='lavash'),InlineKeyboardButton('Burger ',callback_data='burger')],
#         [InlineKeyboardButton('Hoddog ',callback_data='hoddog'),InlineKeyboardButton('Coca cola ',callback_data='coca cola')],
#         [InlineKeyboardButton('Delete',callback_data='delete')]
#     ]
#     return InlineKeyboardMarkup(fastfood_buttons)
#
# def inline_buttons_fastfood_photo():
#     photo_buttons=[
#         [InlineKeyboardButton('Add to cart',callback_data='addtocart'),InlineKeyboardButton('Cancel ',callback_data='cancel')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(photo_buttons)
#
#
# # bu yerga har biriga ichki qisim inline buttons funksiyalarini yozamiz
# def inline_buttons_lavash():
#     lavash_buttons=[
#         [InlineKeyboardButton('Lavash 1',callback_data='lavash1'),InlineKeyboardButton('Lavash 2 ',callback_data='lavash2')],
#         [InlineKeyboardButton('Lavash 3 ',callback_data='lavash3'),InlineKeyboardButton('Lavash 4 ',callback_data='lavash4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(lavash_buttons)
#
# def inline_buttons_burger():
#     burger_buttons=[
#         [InlineKeyboardButton('Burger 1',callback_data='burger1'),InlineKeyboardButton('Burger 2',callback_data='burger2')],
#         [InlineKeyboardButton('Burger 3',callback_data='burger3'),InlineKeyboardButton('Burger 4',callback_data='burger4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(burger_buttons)
#
# def inline_buttons_hoddog():
#     hoddog_buttons=[
#         [InlineKeyboardButton('Hoddog 1',callback_data='hoddog1'),InlineKeyboardButton('Hoddog 2',callback_data='hoddog2')],
#         [InlineKeyboardButton('Hoddog 3',callback_data='hoddog3'),InlineKeyboardButton('Hoddog 4',callback_data='hoddog4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(hoddog_buttons)
#
# def inline_buttons_cocacola():
#     cocacola_buttons=[
#         [InlineKeyboardButton('Coca cola 1',callback_data='cocacola1'),InlineKeyboardButton('Coca Cola 2',callback_data='cocacola2')],
#         [InlineKeyboardButton('Coca cola 3',callback_data='cocacola3'),InlineKeyboardButton('Coca Cola 4',callback_data='cocacola4')],
#         [InlineKeyboardButton('Back',callback_data='back')]
#     ]
#     return InlineKeyboardMarkup(cocacola_buttons)
#
# # Function qismi
#
# def command_outline_buttons(update, context):
#     update.message.reply_text('Assalomu alaykum',reply_markup=outline_buttons_fastfood())
#     return 'message_filters_regex'
#
#
# def message_filters_regex(update,context):
#     update.message.reply_text('Fastfood turlar',reply_markup=inline_buttons_fastfood())
#     return 'callbackquery_in_value'
#
#
# def callbackquery_in_value(update,context):
#     query=update.callback_query
#     print(query.data)
#     # query.message.delete()
#
#     if query.data == 'lavash':
#         query.edit_message_text(text=f"Bo\'lim : {query.data} ",reply_markup=inline_buttons_lavash())
#
#     elif query.data=='burger':
#         query.edit_message_text(text=f"Bo\'lim : {query.data}", reply_markup=inline_buttons_burger())
#     elif query.data=='hoddog':
#         query.edit_message_text(text=f"Bo\'lim :{query.data}", reply_markup=inline_buttons_hoddog())
#     elif query.data=='coca cola':
#         query.edit_message_text(text=f"Bo\'lim :{query.data}", reply_markup=inline_buttons_cocacola())
#
#     elif query.data=='back':
#         query.edit_message_text(text='Fastfood turlari', reply_markup=inline_buttons_fastfood())
#
#     elif query.data=='delete':
#        query.message.delete()
#
#     elif query.data=='lavash1':
#         query.message.reply_photo(photo='https://www.industrialempathy.com/img/remote/ZiClJf-1920w.jpg', caption=f" Bu :{query.data} ",reply_markup=inline_buttons_fastfood_photo())
#         query.message.delete()
#     elif query.data=='lavash2':
#         query.message.reply_photo(photo='https://www.industrialempathy.com/img/remote/ZiClJf-1920w.jpg', caption=f"Bu :{query.data} ",reply_markup=inline_buttons_fastfood_photo())
#         query.message.delete()
#     elif query.data=='lavash3':
#         query.message.reply_photo(photo='https://www.industrialempathy.com/img/remote/ZiClJf-1920w.jpg', caption=f"Bu : {query.data}",reply_markup=inline_buttons_fastfood_photo())
#         query.message.delete()
#     elif query.data=='lavash4':
#         query.message.reply_photo(photo='https://www.industrialempathy.com/img/remote/ZiClJf-1920w.jpg', caption=f"Bu :{query.data}",reply_markup=inline_buttons_fastfood_photo())
#         query.message.delete()
#     elif query.data=='back':
#         query.edit_message_text(text='Lavash turlari', reply_markup=inline_buttons_fastfood())
#
#     elif query.data == 'back1':
#         query.edit_message_text(text='Lavash turlari', reply_markup=inline_buttons_fastfood())
#
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_outline_buttons)
#     ],
#     states={
#         'message_filters_regex':[
#             MessageHandler(Filters.regex('^('+ 'Enter' +')$'),message_filters_regex),
#         ],
#         'callbackquery_in_value':[
#
#             CallbackQueryHandler(callbackquery_in_value)
#         ],
#
#     },
#     fallbacks=[
#         CommandHandler('start',command_outline_buttons)
#     ]
# )
# updater.dispatcher.add_handler(conv_handler)
# updater.start_polling()
# updater.idle()




#//////       SEND CONTACT to BOT   ///////       request_contact=True  qismini yozish kerak         //////////
# ////      KeyboardButton(p1,p2), p1,p2-parameters, p1=text, p2=request_contact=True     /////
# from telegram import ReplyKeyboardMarkup,KeyboardButton,Update
# from telegram.ext import CommandHandler,ConversationHandler,Updater
#
# updater=Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def phone_number():
#     phone_buttons=[
#         [KeyboardButton('SEND CONTACNT',request_contact=True)]
#     ]
#     return ReplyKeyboardMarkup(phone_buttons,resize_keyboard=True)
#
# def command_send_phone(update,context):
#     update.message.reply_text('Bizning botimizga hush kelibsiz',reply_markup=phone_number())
#     return
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_send_phone)
#     ],
#     states={
#
#     },
#     fallbacks=[
#         CommandHandler('start',command_send_phone)
#     ]
#
# )
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()

#//////       SEND LOCATION to BOT     //////        request_location=True            ///////////////////////
# /////   KeyboardButton(p1,p2), p1,p2-parametrlar, p1=text,p2=request_location_True   ////
# from telegram import ReplyKeyboardMarkup,KeyboardButton,Update
# from telegram.ext import CommandHandler,ConversationHandler,Updater
#
# updater=Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def phone_number():
#     phone_buttons=[
#         [KeyboardButton('SEND LOCATION ',request_location=True)]
#     ]
#     return ReplyKeyboardMarkup(phone_buttons,resize_keyboard=True)
#
# def command_phone_send(update,context):
#     update.message.reply_text('Bizning botimizga hush kelibsiz',reply_markup=phone_number())
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_phone_send)
#     ],
#     states={
#
#     },
#     fallbacks=[
#         CommandHandler('start',command_phone_send)
#     ]
#
# )
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()

#/////  SEND CONTACT to BOT and GET PHONE NUMBER from BOT      /////////////////
# MessageHandler(p1,p2), p1=Filters.contact, p2-function
# from telegram import ReplyKeyboardMarkup,KeyboardButton,Update,ReplyKeyboardRemove
# from telegram.ext import CommandHandler,ConversationHandler,Updater,MessageHandler,Filters
#
#
# updater=Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def phone_number():
#     phone_buttons=[
#         [KeyboardButton('SEND CONTACNT',request_contact=True)]
#     ]
#     return ReplyKeyboardMarkup(phone_buttons,resize_keyboard=True)
#
# def command_send_contact(update,context):
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}',reply_markup=phone_number())
#
#     return 'message_get_phone_number'
#
# def message_get_phone_number(update,context):
#     contact=update.effective_message.contact
#     phone=contact.phone_number
#     # nomerni qaytarish
#     update.message.reply_text('This is your telefon number')
#     update.message.reply_text(phone)
#
#     # SEND CONTACT tugmachasini uchirish ReplyKeyboardRemove()- Tashqi buttonni Olib tashlovchi funksiy.
#     update.message.reply_text('Botimizga hush kelibsiz', reply_markup=ReplyKeyboardRemove())
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',command_send_contact)
#     ],
#     states={
#         'message_get_phone_number':[
#             MessageHandler(Filters.contact,message_get_phone_number)
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',command_send_contact)
#     ]
#
# )
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()























