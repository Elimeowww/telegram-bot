from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args and args[0] == "manhwa1":
        await update.message.reply_text("📦 فایل در حال ارسال...")

        await update.message.reply_document(
            document=open("Ch01_ Song Of The Wasteland Farsi-{AoiSekai}", "rb")
        )
    else:
        await update.message.reply_text("سلام 👋")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
