from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

# اینجا فایل‌هات رو می‌ذاری
FILES = {
    "manhwa1": "FILE_ID_1",
    "manhwa2": "FILE_ID_2",
    "chapter3": "FILE_ID_3"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args:
        key = args[0]

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")

            await update.message.reply_document(
                document=FILES[key]
            )
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")
    else:
        await update.message.reply_text("سلام 👋")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
