# other libs
import counting_objects
import objectList

# imports
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ContextTypes, CallbackContext, CallbackQueryHandler

# token
BotToken = "5734069935:AAE-Mgda8Xl4-c9vcWGpGt7HI8DrfjsUI-8"


# functions
def start(update, context):
    sticker = open('static/welcome.webp', 'rb')
    update.message.reply_sticker(sticker)

    update.message.reply_text(
        f"Welcome, {update.message.chat.first_name}!\nI am - MyCount a bot that will help you count the "
        "number of objects in the photo.")

    update.message.reply_text('References:', reply_markup=keyboard_main_menu())


def help(update, context):
    update.message.reply_text("Send me a picture.\n<b>I can only see:</b>"
                              f"\n\n{objectList.list}")
    # update.reply_text(update.message.chat.id, 'Send me a picture🙏🙏🙏')


# photo processing
def document(update, context):
    with open("static/image.jpg", 'wb') as new_file:
        context.bot.get_file(update.message.document).download(out=new_file)

    update.message.reply_text(counting_objects.count_obj())
    update.message.reply_photo(photo=open('static/result.jpg', 'rb'))


def photo(update, context):
    with open("static/image.jpg", 'wb') as new_file:
        context.bot.get_file(update.message.photo[-1].file_id).download(out=new_file)

    update.message.reply_text(counting_objects.count_obj())
    update.message.reply_photo(photo=open('static/result.jpg', 'rb'))


# photo processing end


# keyboard
def main_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='References:',
                            reply_markup=keyboard_main_menu())


def keyboard_main_menu():
    keyboard = [
        [InlineKeyboardButton("Link to GitHub", callback_data='Link to GitHub'),
         InlineKeyboardButton("Authors", callback_data='Authors'), ],
    ]

    return InlineKeyboardMarkup(keyboard)


def Link_to_GitHub(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Main menu", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text="<a href='https://github.com/kooofe/TelegramProject'>Link</a>",
                            parse_mode=ParseMode.HTML, reply_markup=reply_markup)


def Authors(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Main menu", callback_data='main')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"{query.data}:\n"
                                 f"Zhanibek Meiramkan, Laura Sepbossynova, Arlan Manap, Diana Balchikbayeva.",
                            reply_markup=reply_markup, )


# keyboard end

def main():
    updater = Updater(BotToken, use_context=True)
    dp = updater.dispatcher

    # functions
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # data progress
    dp.add_handler(MessageHandler(Filters.photo, photo))
    dp.add_handler(MessageHandler(Filters.document, document))
    # keyboard
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(Link_to_GitHub, pattern='Link to GitHub'))
    dp.add_handler(CallbackQueryHandler(Authors, pattern='Authors'))
    # run
    updater.start_polling(timeout=60)
    updater.idle()


# start project
if __name__ == '__main__':
    main()
