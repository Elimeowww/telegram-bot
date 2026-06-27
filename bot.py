from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

# فایل‌ها (اینجا مسیر یا file_id میتونه باشه)
FILES = {
    "manhwa1": "file1.pdf",
    "manhwa2": "file2.pdf"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    # اگر لینک اختصاصی بود
    if args:
        key = args[0]

        if key in FILES:
            file_name = FILES[key]

            keyboard = [
                [InlineKeyboardButton("📥 دانلود فایل", callback_data=key)]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            await update.message.reply_text(
                "فایل آماده است 👇",
                reply_markup=reply_markup
            )
        else:
            await update.message.reply_text("فایل پیدا نشد ❌")

    else:
        await update.message.reply_text("سلام 👋\nلینک فایل بفرست یا /start manhwa1")

async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    key = query.data

    file_path = FILES.get(key)

    if file_path:
        await query.message.reply_document(document=InputFile(file_path))
    else:
        await query.message.reply_text("فایل موجود نیست ❌")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("file", send_file))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
