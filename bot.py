from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

# 📦 دیتابیس فایل‌ها (بعداً اینجا file_id ها رو می‌ذاری)
FILES = {
    "manhwa1": "BQACAgQAAxkBAAMeaj_vLiiqQ3fOIIvTbIJsel2CC7wAAlcrAAL5jgFSHMyEWa9ZDbk8BA",
    "manhwa2": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
}

# 🔵 استارت اصلی
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    # اگر لینک داشت
    if args:
        key = args[0]

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(document=FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")

    # استارت معمولی
    else:
        await update.message.reply_text(
            "سلام 👋\n\n"
            "برای دریافت فایل از لینک استفاده کن.\n\n"
            "یا فایل بفرست برای گرفتن FILE_ID"
        )

# 🟢 گرفتن FILE_ID از فایل‌هایی که می‌فرستی
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document

    if file:
        await update.message.reply_text(
            f"📦 FILE_ID شما:\n\n`{file.file_id}`",
            parse_mode="Markdown"
        )

# 🚀 اجرا
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
