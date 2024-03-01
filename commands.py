from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

import config

BOT_TOKEN = config.BOT_TOKEN

user_dates = {}


def start(update, context):
    """Command handler for the /start command."""
    user = update.message.from_user
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"Hello {user.first_name}! This is your bot.")
    
def settime(update, context):
    keyboard = [
        [InlineKeyboardButton("Select Start Date", callback_data='start_date')],
        [InlineKeyboardButton("Select End Date", callback_data='end_date')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Please choose a start date and an end date:", reply_markup=reply_markup)

def button_click(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    user_id = query.from_user.id

    if query.data == 'start_date':
        context.bot.send_message(chat_id=chat_id, text="Please select the start date.")
        user_dates[user_id] = {'start_date': None, 'end_date': None}
    elif query.data == 'end_date':
        context.bot.send_message(chat_id=chat_id, text="Please select the end date.")
    else:
        return
    
def handle_date(update, context):
    user_id = update.message.from_user.id

    # Assume the message text contains the selected date for simplicity
    selected_date = update.message.text

    if 'start_date' in user_dates[user_id] and user_dates[user_id]['start_date'] is None:
        user_dates[user_id]['start_date'] = selected_date
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Start date set to: {selected_date}")
    elif 'end_date' in user_dates[user_id] and user_dates[user_id]['end_date'] is None:
        user_dates[user_id]['end_date'] = selected_date
        context.bot.send_message(chat_id=update.message.chat_id, text=f"End date set to: {selected_date}")


def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("settime", settime))
    dp.add_handler(CallbackQueryHandler(button_click))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_date))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# Select time range for new notifications
# Select esindused