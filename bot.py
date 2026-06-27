from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

FILES = {
    "manhwa1": "FILE_ID_1",
    "manhwa25": "BQACAgQAAxkBAANTakAIpqeymmDk1IQAAXbDrxEe1m1fAAI8GAACtFn4UarzHCrgfAS-PAQ",
    "manhwa3": "FILE_ID_3"
}

# 🚀 استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args:
        key = args[0]

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(document=FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")
    else:
        await update.message.reply_text("سلام 👋\nفایل بفرست تا ID بدم")

# 🟢 گرفتن file_id (نسخه دقیق‌تر)
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        file_id = update.message.document.file_id

        await update.message.reply_text(
            f"📦 FILE_ID:\n{file_id}"
        )

    else:
        await update.message.reply_text("❌ این فایل نیست")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # ⚠️ این مهم‌ترین خطه
    app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
