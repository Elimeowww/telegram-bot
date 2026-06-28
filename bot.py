from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8769525491:AAH2Nh6T_ubofOXVUkO1rethXZcwaSVv24U"

ADMIN_ID = 8256304031  # آیدی عددی خودت

FILES = {
    "manhwa132": "BQACAgQAAxkBAAOqakD94Gjhf9IY14k_ioEFmsBbFKoAAs4eAAK09AlSsFgEqZGBt0w8BA",
    "manhwa2": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
}


# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    # اگر لینک دانلود بود
    if args:
        key = args[0]

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(document=FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")

        return

    # اگر استارت معمولی بود
    if user_id != ADMIN_ID:
        return

    await update.message.reply_text(
        "👑 پنل ادمین فعال شد\n\n"
        "📄 فایل بفرست تا FILE_ID آن را بگیری."
    )


# گرفتن FILE_ID فقط برای ادمین
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if update.message.document:
        await update.message.reply_text(
            f"📦 FILE_ID:\n\n{update.message.document.file_id}"
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
