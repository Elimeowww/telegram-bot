from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8769525491:AAH2Nh6T_ubofOXVUkO1rethXZcwaSVv24U"
ADMIN_ID = 8256304031

CHANNEL = "@gaptestes"

FILES = {
    "manhwa132": "BQACAgQAAxkBAAOqakD94Gjhf9IY14k_ioEFmsBbFKoAAs4eAAK09AlSsFgEqZGBt0w8BA"
}


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

    # 👇 اگر لینک بود
    if args:
        key = args[0]

        # ❌ اگر عضو نیست
        if not await is_member(bot, user_id):
            keyboard = [
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")],
            ]
            await update.message.reply_text(
                "❌ اول عضو کانال شو بعد دوباره امتحان کن",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return

        # 📦 ارسال فایل
        if key in FILES:
            await update.message.reply_document(FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")

        return

    # 👑 ادمین
    if user_id == ADMIN_ID:
        await update.message.reply_text("👑 پنل ادمین فعال شد")
        return

    # 👥 کاربر معمولی
    await update.message.reply_text("سلام 👋 لینک فایل بفرست")


# 📝 برای متن‌های معمولی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    bot = context.bot

    # ❌ اگر عضو نیست
    if not await is_member(bot, user_id):
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")],
        ]
        await update.message.reply_text(
            "❌ اول عضو کانال شو بعد دوباره امتحان کن",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # 📦 ارسال فایل
    if text in FILES:
        await update.message.reply_document(FILES[text])
    else:
        await update.message.reply_text("❌ فایل پیدا نشد")


# 🤖 اپلیکیشن
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
# ✅ این خط رو اضافه کن:
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
