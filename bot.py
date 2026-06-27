from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

# 📌 کانال اجباری (حتماً @ بگذار)
CHANNEL_USERNAME = "@YourChannel"

FILES = {
    "manhwa1": "FILE_ID_1",
    "manhwa25": "BQACAgQAAxkBAANTakAIpqeymmDk1IQAAXbDrxEe1m1fAAI8GAACtFn4UarzHCrgfAS-PAQ",
    "manhwa3": "FILE_ID_3"
}

# 🔍 چک عضویت کاربر
async def check_membership(bot, user_id):
    try:
        member = await bot.get_chat_member("https://t.me/gaptestes", "@gaptestes")
        return member.status in ["member", "creator", "administrator"]
    except:
        return False

# 🚀 استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    is_member = await check_membership(bot, user_id)

    if not is_member:
        await update.message.reply_text(
            f"❌ برای استفاده از ربات باید عضو کانال زیر بشی:\n\n{CHANNEL_USERNAME}\n\nبعد دوباره /start بزن"
        )
        return

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
        await update.message.reply_text("سلام 👋\nلینک فایل رو بزن")

# 🟢 گرفتن file_id
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        await update.message.reply_text(
            f"📦 FILE_ID:\n{update.message.document.file_id}"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
