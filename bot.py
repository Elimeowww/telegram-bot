from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = "8769525491:AAH2Nh6T_ubofOXVUkO1rethXZcwaSVv24U"
ADMIN_ID = 8256304031

CHANNEL = "@gaptestes"

FILES = {
    "manhwa132": "BQACAgQAAxkBAAOqakD94Gjhf9IY14k_ioEFmsBbFKoAAs4eAAK09AlSsFgEqZGBt0w8BA",
    "manhwa2": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
}


def is_admin(user_id):
    return user_id == ADMIN_ID


# 🔍 چک عضویت
async def is_member(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False


# 🚀 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    bot = context.bot

    # 📦 اگر لینک فایل بود
    if args:
        key = args[0]

        # ❌ اگر عضو نیست
        if not await is_member(bot, user_id):
            keyboard = [
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")],
                [InlineKeyboardButton("✅ عضو شدم", callback_data=f"check_{key}")]
            ]
            await update.message.reply_text(
                "❌ برای دریافت فایل باید عضو کانال شوی:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return

        # 📦 ارسال فایل
        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")

        return

    # 👑 ادمین
    if is_admin(user_id):
        await update.message.reply_text("👑 پنل ادمین فعال شد")


# 🚀 اجرا
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
