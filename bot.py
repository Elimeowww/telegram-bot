from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8871850096:AAFTf5tNLFOimNCXDWCRXl1-XvzV3TILzvg"
ADMIN_ID = 8256304031
PORT = int(os.getenv("PORT", 8000))
RAILWAY_URL = os.getenv("RAILWAY_PUBLIC_DOMAIN", "http://localhost:8000")

FILES = {}  # 🟡 فایل‌ها اینجا ذخیره میشن


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    # 👑 فقط ادمین
    if user_id == ADMIN_ID:
        await update.message.reply_text(
            "👑 سلام ادمین!\n\n"
            "🔹 فایل بفرست تا کدش رو بهت بدم\n"
            "🔹 یا /files برای دیدن فایل‌های موجود"
        )
    else:
        # 🚫 بقیه کاربران
        pass  # هیچ چیز

