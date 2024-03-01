from telegram.ext import Updater, CommandHandler
import config

BOT_TOKEN = config.BOT_TOKEN

def start(update, context):
    """Command handler for the /start command."""
    user = update.message.from_user
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f"Hello {user.first_name}! This is your bot.")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
