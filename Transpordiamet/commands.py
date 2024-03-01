from telegram.ext import Updater, CommandHandler
import config

BOT_TOKEN = config.BOT_TOKEN

def start(update, context):
    """Command handler for the /start command."""
    user = update.message.from_user
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"Hello {user.first_name}! This is your bot.")

def set_time1(update, context):
    """Command handler for settime1."""
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You selected settime1.")

def set_time2(update, context):
    """Command handler for settime2."""
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You selected settime2.")

def set_time3(update, context):
    """Command handler for settime3."""
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You selected settime3.")

def set_time4(update, context):
    """Command handler for settime4."""
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You selected settime4.")

def set_time5(update, context):
    """Command handler for settime5."""
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="You selected settime5.")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("settime1", set_time1))
    dp.add_handler(CommandHandler("settime2", set_time2))
    dp.add_handler(CommandHandler("settime3", set_time3))
    dp.add_handler(CommandHandler("settime4", set_time4))
    dp.add_handler(CommandHandler("settime5", set_time5))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
