from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

CHANNEL = "@gaptestes"  # 👈 کانال اینجا

FILES = {
    "manhwa1": "FILE_ID_1",
    "manhwa25": "BQACAgQAAxkBAANTakAIpqeymmDk1IQAAXbDrxEe1m1fAAI8GAACtFn4UarzHCrgfAS-PAQ",
    "manhwa3": "FILE_ID_3"
}

# 🟢 چک عضویت
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

    # چک عضویت
    if not await is_member(bot, user_id):
        await update.message.reply_text(
            f"❌ برای استفاده از ربات باید عضو کانال زیر بشی:\n\n{CHANNEL}"
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
        await update.message.reply_text("سلام 👋")

# 🚀 اجرا
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
