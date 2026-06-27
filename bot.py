from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

# 📦 اینجا فایل‌هات رو اضافه می‌کنی
FILES = {
    "manhwa1": "BQACAgQAAxkBAAMeaj_vLiiqQ3fOIIvTbIJsel2CC7wAAlcrAAL5jgFSHMyEWa9ZDbk8BA",
    "manhwa2": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
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
            await update.message.reply_text("❌ این فایل وجود ندارد")
    else:
        await update.message.reply_text(
            "سلام 👋\nلینک فایل رو بفرست یا از کانال وارد شو"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
