import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# קבלת הטוקן מהסביבה (Render או מקומית)
TOKEN = os.environ.get("8395742526:AAEsUoSXNzL8LYQN3Cn2lLEb-syoy54LfgA")

def start(update, context):
    update.message.reply_text("🎉 ברוכים הבאים לבוט הגשר שלנו! זהו שער לעולם של אמת, לא זיופים!")

def help_command(update, context):
    update.message.reply_text("🔥 הבוט שלנו מפנה אותך רק לדברים מקוריים.\nכדי להתחיל השתמש ב־/start")

def unknown(update, context):
    update.message.reply_text("🤖 לא הבנתי את הפקודה הזאת. נסה /start או /help")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
