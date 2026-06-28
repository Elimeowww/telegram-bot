from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8769525491:AAH2Nh6T_ubofOXVUkO1rethXZcwaSVv24U"

ADMIN_ID = 8256304031  # 👈 آیدی خودت

# 📢 کانال‌های اجباری
CHANNELS = "@gaptestes"
    

FILES = {
    "manhwa132": "BQACAgQAAxkBAAOqakD94Gjhf9IY14k_ioEFmsBbFKoAAs4eAAK09AlSsFgEqZGBt0w8BA",
    "manhwa2": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
}

# 🟢 چک ادمین
def is_admin(user_id):
    return user_id == ADMIN_ID

# 🟢 چک عضویت در همه کانال‌ها
async def is_member(bot, user_id):
    try:
        for ch in CHANNELS:
            member = await bot.get_chat_member(ch, user_id)
            if member.status not in ["member", "creator", "administrator"]:
                return False
        return True
    except:
        return False

# 🚀 استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    bot = context.bot

    # 📦 اگر لینک دانلود بود
    if args:
        key = args[0]

        # ❌ اگر عضو کانال نیست
        if not await is_member(bot, user_id):
            return

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(document=FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")
        return

    # 👑 پنل فقط برای ادمین
    if is_admin(user_id):
        await update.message.reply_text(
            "👑 پنل ادمین فعال شد\n"
            "📌 فایل بفرست تا FILE_ID بگیری"
        )

    # 👥 بقیه هیچ پیامی نمی‌بینند
    return

# 🟢 گرفتن FILE_ID فقط برای ادمین
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if update.message.document:
        await update.message.reply_text(
            f"📦 FILE_ID:\n{update.message.document.file_id}"
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
