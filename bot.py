from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8871850096:AAFfAuWjR1BPHTOkCeNxLuFtH2lpxTmJpck"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! فایل بفرست")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id
        file_name = update.message.document.file_name
        
        await update.message.reply_text(
            f"✅ فایل دریافت شد!\n\n"
            f"📝 نام: {file_name}\n"
            f"🔑 کد: {file_id}"
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    
    app.run_polling()
