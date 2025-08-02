from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")  # Replace with your actual bot token

def start(update, context):
    update.message.reply_text("Welcome to Treshener Bot 🌌 This is your gateway to original product!")

def help_command(update, context):
    update.message.reply_text("This bot is a bridge to real stuff, not fake junk. Use /start to begin.")

def unknown(update, context):
    update.message.reply_text("Sorry, I don't recognize that command. Try /start or /help.")

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler(None, unknown))

updater.start_polling()
updater.idle()
