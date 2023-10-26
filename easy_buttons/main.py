
# 1)  /////  Assisiy ma'lumotlarni olish botdan  ///////////////////////////////////////////////////
# from telegram import Update
# from telegram.ext import Updater, CommandHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def start_main(update, context):
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}')
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.last_name}')
#     update.message.reply_text(f' sizning Id raqamingiz - {update.effective_user.id} ')
#     update.message.reply_text(f' sizning language codingiz - {update.effective_user.language_code} ')
#     update.message.reply_text(f' siz botmisiz - {update.effective_user.is_bot} ')
#
# updater.dispatcher.add_handler(CommandHandler('start', start_main))
#
# updater.start_polling()
# updater.idle()

# 2)  ////////  bunda yozilgan message ni prosta uzizga qaytarib(echo) qilib beradi hechqayerga junatib bo'lmaydi  ////////////////////////////////

# from telegram import Update
# from telegram.ext import Updater,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def echo_fun (update,context):
#     message=update.message.text
#     update.message.reply_text(message)
#
# updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=echo_fun))
#
# updater.start_polling()
# updater.idle()

# 3) ////  bunda yozilgan messageni  chat_id - li user ga junatadi      ///////////////
# from telegram import Update
# from telegram.ext import Updater,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def echo_fun (update,context):
#     message=update.message.text
#     context.bot.send_message(text=message,chat_id=update.effective_user.id)
#
# updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=echo_fun))
#
# updater.start_polling()
# updater.idle()

# 4) ////   Bu yerda chat_id -ga son qiymat quyilgan, message shu chat_id li user ga boradi               ////////////////////////////

# from telegram import Update
# from telegram.ext import Updater,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def echo_fun (update,context):
#     message=update.message.text
#
#     context.bot.send_message(text=message,chat_id=409412968)
#
# updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=echo_fun))
#
# updater.start_polling()
# updater.idle()

# 5) ///////////////////////////////////////////////////////////////////////
# from telegram import Update
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def start(update, context):
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}')
#
# def echo_fun (update,context):
#     message=update.message.text
#
#     if update.effective_user.id==409412968:
#
#         context.bot.send_message(text=message,chat_id=83569311)
#     else:
#         context.bot.send_message(text=message,chat_id=409412968)
#
#
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=echo_fun))
#
#
# updater.start_polling()
# updater.idle()

# 6) ///////                                                   ///////////////////////////////////////////
# from telegram import Update
# from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def start(update,context):
#     update.message.reply_text('Assalomu alaykum')
#
# def command_set(update,context):
#     update.message.reply_text('ok vaqtni sekundlarda yuboring')
#
# def echo_fun (update,context):
#     message=update.message.text
#     chat_id = update.effective_user.id
#     if message.isdigit():
#         context.job_queue.run_once(alarm,int(message),context=chat_id,name=str(chat_id))
#
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
#
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('set', command_set))
# updater.dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=echo_fun))
#
# updater.start_polling()
# updater.idle()

# 7) ///////////////////////////////////////////////////////////////////////////////////

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# def start(update,context):
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}')
#     return 'settime'
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
# def sendtime(update,context):
#     message = update.message.text
#     chat_id = update.effective_user.id
#     print(message.isdigit())
#     if message.isdigit():
#         context.job_queue.run_once(alarm, int(message), context=chat_id, name=str(chat_id))
#         update.message.reply_text('Vaqt  muaffaqiyatli urnatildi')
#
#     else:
#         context.bot.send_message(text="Siz notug'ri farmatda kiritdingiz iltimos vaqtni raqamlarda qayttadan kiriting",chat_id=update.effective_user.id)
#
# def command_set(update,context):
#     update.message.reply_text('Ok, vaqtni sekundlarda yuboring')
#     return 'sendtime'
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',start)
#
#     ],
#     states={
#         'settime':[
#             CommandHandler('set',command_set)
#         ],
#         'sendtime':[
#             MessageHandler(Filters.text,sendtime)
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',start)
#     ]
# )
#
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()

# 8)  ///////////////////////////////////////////////////////////////////////////////////

# from telegram import Update,ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
# buttons=[
#     ['set time','delete time'],
#     ['delete time'],
# ]
#
# def start(update, context):
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name}',reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True))
#     return 'settime'
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
# def sendtime(update,context):
#     message = update.message.text
#     chat_id = update.effective_user.id
#     print(message.isdigit())
#     if message.isdigit():
#         context.job_queue.run_once(alarm, int(message), context=chat_id, name=str(chat_id))
#         update.message.reply_text('Vaqt  muaffaqiyatli urnatildi')
#
#     else:
#         context.bot.send_message(text="Siz notug'ri farmatda kiritdingiz iltimos vaqtni raqamlarda qayttadan kiriting",chat_id=update.effective_user.id)
#
# def command_set(update,context):
#     update.message.reply_text('Ok, vaqtni sekundlarda yuboring')
#     return 'sendtime'
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',start)
#
#     ],
#     states={
#         'settime':[
#             MessageHandler(Filters.regex('^('+ 'set time' +')$'),command_set)
#         ],
#         'sendtime':[
#             MessageHandler(Filters.text,sendtime)
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',start)
#     ]
# )
#
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()


# 9) /////////////////////////////////////////////////////////////////////
# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# reply_buttons=[
#     ['set time']
# ]
#
# inline_buttons=[
#     [InlineKeyboardButton('set time',callback_data='set time')]
#
# ]
#
# def start(update,context):
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \n ICT o\'quv markazining rasmiy telegram botiga hush kelibsiz',reply_markup=ReplyKeyboardMarkup(reply_buttons,resize_keyboard=True))
#     return 'settime'
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
# def sendtime(update,context):
#     message = update.message.text
#     chat_id = update.effective_user.id
#     print(message.isdigit())
#     if message.isdigit():
#         context.job_queue.run_once(alarm, int(message), context=chat_id, name=str(chat_id))
#         update.message.reply_text('Vaqt  muaffaqiyatli urnatildi')
#
#     else:
#         context.bot.send_message(text="Siz notug'ri farmatda kiritdingiz iltimos vaqtni raqamlarda qayttadan kiriting",chat_id=update.effective_user.id)
#
# def command_set(update,context):
#     update.message.reply_text('Ok, vaqtni sekundlarda yuboring',reply_markup=InlineKeyboardMarkup(inline_buttons))
#     return 'sendtime'
#
# def inline_button_callbak(update,context):
#     query=update.callback_query
#     print(query.data)
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',start)
#
#     ],
#     states={
#         'settime':[
#             MessageHandler(Filters.regex('^('+ 'set time' +')$'),command_set)
#         ],
#         'sendtime':[
#             MessageHandler(Filters.text,sendtime),
#             CallbackQueryHandler(inline_button_callbak)
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',start)
#     ]
# )
#
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()


# 10)  /////////////////////////////////////////////////////////////////////
# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
#
# reply_buttons=[
#     ['set time','delete time'],
#     ['delete time'],
# ]
#
# inline_buttons=[
#     [InlineKeyboardButton('set time',callback_data='set time'),InlineKeyboardButton('delete time',callback_data='delete time')],
#     [InlineKeyboardButton('send time',callback_data='send time')],
#
# ]
#
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \n ICT o\'quv markazining rasmiy telegram botiga hush kelibsiz',reply_markup=ReplyKeyboardMarkup(reply_buttons,resize_keyboard=True))
#     return 'settime'
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
# def sendtime(update,context):
#     message = update.message.text
#     chat_id = update.effective_user.id
#     print(message.isdigit())
#
#
#     if message.isdigit():
#         context.job_queue.run_once(alarm, int(message), context=chat_id, name=str(chat_id))
#         update.message.reply_text('Vaqt  muaffaqiyatli urnatildi')
#
#     else:
#         context.bot.send_message(text="Siz notug'ri farmatda kiritdingiz iltimos vaqtni raqamlarda qayttadan kiriting",chat_id=update.effective_user.id)
#
# def command_set(update,context):
#     update.message.reply_text('Ok, vaqtni sekundlarda yuboring',reply_markup=InlineKeyboardMarkup(inline_buttons))
#     return 'sendtime'
#
# def inline_button_callbak(update,context):
#     query=update.callback_query
#     print(query.data)
#     if query.data=='set time':
#         query.message.reply_html("<b>set time tugmachasi bosildi</b>")
#     elif query.data=='delete time':
#         query.message.reply_html("<b>delete tugmachasi bosildi</b>")
#     elif query.data=='send time':
#         query.message.reply_html("<b>send time tugmachasi bosildi</b>")
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',start)
#
#     ],
#     states={
#         'settime':[
#             MessageHandler(Filters.regex('^('+ 'set time' +')$'),command_set)
#         ],
#         'sendtime':[
#             MessageHandler(Filters.text,sendtime),
#             CallbackQueryHandler(inline_button_callbak),
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',start)
#     ]
# )
#
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()


# 11)   ////////////////////////////////////////////////////////////////////
# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
#
# reply_buttons=[
#     ['set time','delete time'],
#     ['delete time'],
# ]
#
# inline_buttons=[
#     [InlineKeyboardButton('set time',callback_data='set time'),InlineKeyboardButton('delete time',callback_data='delete time')],
#     [InlineKeyboardButton('send time',callback_data='send time')],
#
# ]
#
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \n ICT o\'quv markazining rasmiy telegram botiga hush kelibsiz',reply_markup=ReplyKeyboardMarkup(reply_buttons,resize_keyboard=True))
#     return 'settime'
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
# def sendtime(update,context):
#     message = update.message.text
#     chat_id = update.effective_user.id
#     print(message.isdigit())
#
#
#     if message.isdigit():
#         context.job_queue.run_once(alarm, int(message), context=chat_id, name=str(chat_id))
#         update.message.reply_text('Vaqt  muaffaqiyatli urnatildi')
#
#     else:
#         context.bot.send_message(text="Siz notug'ri farmatda kiritdingiz iltimos vaqtni raqamlarda qayttadan kiriting",chat_id=update.effective_user.id)
#
# def command_set(update,context):
#     update.message.reply_text('Ok, vaqtni sekundlarda yuboring',reply_markup=InlineKeyboardMarkup(inline_buttons))
#     return 'sendtime'
#
# def inline_button_callbak(update,context):
#     query=update.callback_query
#     print(query.data)
#
#     if query.data=='set time':
#         query.message.reply_html("<b>set time tugmachasi bosildi</b>")
#     elif query.data=='delete time':
#         query.message.delete()
#         query.message.reply_html("<b>delete tugmachasi bosildi va habar uchirildi</b>")
#     elif query.data=='send time':
#         query.message.reply_html("<b>send time tugmachasi bosildi</b>")
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',start)
#
#     ],
#     states={
#         'settime':[
#             MessageHandler(Filters.regex('^('+ 'set time' +')$'),command_set)
#         ],
#         'sendtime':[
#             MessageHandler(Filters.text,sendtime),
#             CallbackQueryHandler(inline_button_callbak),
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',start)
#     ]
# )
#
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()

# 12)  /////////////////////////////////////////////////////////////////////
# from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, CallbackContext,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
#
# updater = Updater('5035067903:AAGEU1qbEtM8CvaBc7ZfPnBoC__gCjvuLPg')
#
#
# reply_buttons=[
#     ['set time','delete time'],
#     ['delete time'],
# ]
#
# inline_buttons=[
#     [InlineKeyboardButton('set time',callback_data='set time'),InlineKeyboardButton('delete time',callback_data='delete time')],
#     [InlineKeyboardButton('send time',callback_data='send time')],
#
# ]
#
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \n ICT o\'quv markazining rasmiy telegram botiga hush kelibsiz',reply_markup=ReplyKeyboardMarkup(reply_buttons,resize_keyboard=True))
#     return 'settime'
#
# def alarm(context):
#     job=context.job
#     context.bot.send_message(job.context,text='Siz aytgan vaqt buldi')
#
# def sendtime(update,context):
#     message = update.message.text
#     chat_id = update.effective_user.id
#     print(message.isdigit())
#
#
#     if message.isdigit():
#         context.job_queue.run_once(alarm, int(message), context=chat_id, name=str(chat_id))
#         update.message.reply_text('Vaqt  muaffaqiyatli urnatildi')
#
#     else:
#         context.bot.send_message(text="Siz notug'ri farmatda kiritdingiz iltimos vaqtni raqamlarda qayttadan kiriting",chat_id=update.effective_user.id)
#
# def command_set(update,context):
#     update.message.reply_text('Ok, vaqtni sekundlarda yuboring',reply_markup=InlineKeyboardMarkup(inline_buttons))
#     return 'sendtime'
#
# def inline_button_callbak(update,context):
#     query=update.callback_query
#     print(query.data)
#
#     if query.data=='set time':
#         # query.message.reply_html("<b>set time tugmachasi bosildi</b>")
#         # query.edit_message_text(text='set time')
#         query.edit_message_text(text='set time',reply_markup=InlineKeyboardMarkup(inline_buttons))
#
#     elif query.data=='delete time':
#         query.message.delete()
#         query.message.reply_html("<b>delete tugmachasi bosildi va habar uchirildi</b>")
#     elif query.data=='send time':
#         query.message.reply_html("<b>send time tugmachasi bosildi</b>")
#
#
# conv_handler=ConversationHandler(
#     entry_points=[
#         CommandHandler('start',start)
#
#     ],
#     states={
#         'settime':[
#             MessageHandler(Filters.regex('^('+ 'set time' +')$'),command_set)
#         ],
#         'sendtime':[
#             MessageHandler(Filters.text,sendtime),
#             CallbackQueryHandler(inline_button_callbak),
#         ]
#
#     },
#     fallbacks=[
#         CommandHandler('start',start)
#     ]
# )
#
# updater.dispatcher.add_handler(conv_handler)
#
# updater.start_polling()
# updater.idle()

