from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8871850096:AAE5dxh1wU2aVYva6o9Tlz-K2vIXLgdmHDo"
CHANNEL = "@gaptestes"

# فایل‌ها
FILES = {
    "manwha14": "BQACAgQAAxkBAAIBA2pBEfZBoO8ww5EhmvrTXM8tlxsXAAI3HwACV-UJUnJzplB_2dIGPAQ"
}


async def is_member(bot, user_id):
    """چک کردن عضویت در کانال"""
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """استارت - خالی"""
    pass


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دریافت فایل و ذخیره کد"""
    user_id = update.effective_user.id
    bot = context.bot
    
    # چک عضویت
    if not await is_member(bot, user_id):
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")]
        ]
        await update.message.reply_text(
            "❌ لطفاً اول عضو کانال شو",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return
    
    # اگر فایل باشه
    if update.message.document:
        file_id = update.message.document.file_id
        file_name = update.message.document.file_name
        
        await update.message.reply_text(
            f"✅ فایل ذخیره شد!\n\n"
            f"📝 نام: `{file_name}`\n"
            f"🔑 کد: `{file_id}`"
        )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دریافت متن و ارسال فایل"""
    user_id = update.effective_user.id
    bot = context.bot
    text = update.message.text
    
    # چک عضویت
    if not await is_member(bot, user_id):
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")]
        ]
        await update.message.reply_text(
            "❌ لطفاً اول عضو کانال شو",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return
    
    #

