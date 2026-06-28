from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8871850096:AAG7WEcfdR7Zg-BbmQuBqJdM2BpLtYroMl8"

ADMIN_ID = 8256304031  # 👈 آیدی خودت

CHANNEL = [ 
    "@femboycuteir"
    "https://t.me/+8W6XKgRQyYZkYjlk"
]# (اگر خواستی بعداً فعالش کن)

FILES = {
    "manhwa1": "BQACAgQAAxkBAAOqakD94Gjhf9IY14k_ioEFmsBbFKoAAs4eAAK09AlSsFgEqZGBt0w8BA",
    "manhwa2": "FILE_ID_2",
    "manhwa3": "FILE_ID_3"
}

# 👑 چک ادمین
def is_admin(user_id):
    return user_id == ADMIN_ID

# 🚀 استارت (فقط ادمین می‌بیند)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # ❌ بقیه هیچ چیزی نمی‌بینند
    if not is_admin(user_id):
        return

    await update.message.reply_text(
        "👑 پنل ادمین فعال شد\n"
        "📌 فایل بفرست برای گرفتن FILE_ID\n"
        "📌 یا لینک: /start manhwa1"
    )

# 📦 ارسال فایل برای کاربران (بدون محدودیت پیام start)
async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args:
        key = args[0]

        if key in FILES:
            await update.message.reply_text("📦 در حال ارسال فایل...")
            await update.message.reply_document(document=FILES[key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")

# 🟢 گرفتن FILE_ID فقط برای ادمین
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_admin(user_id):
        return

    if update.message.document:
        await update.message.reply_text(
            f"📦 FILE_ID:\n{update.message.document.file_id}"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("start", send_file))
    app.add_handler(MessageHandler(filters.Document.ALL, get_file_id))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
