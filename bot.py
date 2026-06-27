from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

CHANNEL = "@gaptestes"

# 👑 فقط تو اجازه داری فایل آپلود کنی
ADMIN_ID = 8256304031  # 👈 آیدی عددی خودت اینو عوض کن

FILES = {
    "manhwa1": "FILE_ID_1",
    "manhwa25": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
}

# 🟢 چک عضویت کانال
async def is_member(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False

# 🚀 استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    # ❌ اگر عضو کانال نیست
    if not await is_member(bot, user_id):
        await update.message.reply_text(f"❌ باید عضو کانال بشی:\n{CHANNEL}")
        return

    args = context.args

    if args:
        key = args[0]

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(document=FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")
    else:
        await update.message.reply_text("سلام 👋")

# 🟢 فقط ادمین میتونه فایل بفرسته و file_id بگیره
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # ❌ اگر ادمین نیست
    if user_id != ADMIN_ID:
        return

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
