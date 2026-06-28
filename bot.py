from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8871850096:AAFfAuWjR1BPHTOkCeNxLuFtH2lpxTmJpck"
CHANNELS = "@femboycuteir"

# فایل‌ها
FILES = {
    "manhwa25": "BQACAgQAAxkBAAIBA2pBEfZBoO8ww5EhmvrTXM8tlxsXAAI3HwACV-UJUnJzplB_2dIGPAQ"
}


async def is_member(bot, user_id):
    """چک کردن عضویت"""
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """استارت با لینک"""
    user_id = update.effective_user.id
    bot = context.bot
    args = context.args
    
    # اگر لینک با پارامتر باشه
    if args:
        file_key = args[0]
        
        # چک عضویت
        if not await is_member(bot, user_id):
            keyboard = [
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")]
            ]
            await update.message.reply_text(
                "❌ اول عضو کانال شو، بعدش دوباره لینک رو بزن",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return
        
        # ارسال فایل
        if file_key in FILES:
            await update.message.reply_document(FILES[file_key])
        else:
            await update.message.reply_text("❌ فایل پیدا نشد")
    else:
        # استارت بدون پارامتر
        pass


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    app.run_polling()
