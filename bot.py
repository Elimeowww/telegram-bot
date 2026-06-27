from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("فایل بفرست تا file_id بدم 👇")

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document

    if file:
        await update.message.reply_text(f"📦 FILE_ID:\n{file.file_id}")
    else:
        await update.message.reply_text("این فایل نیست ❌")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
