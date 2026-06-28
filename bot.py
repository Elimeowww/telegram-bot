from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8871850096:AAGOuOUIPOfpdEY5l8oTC-cQtayH1bXdfhA"
ADMIN_ID = 8256304031
CHANNEL = "@gaptestes"  # 🔗 کانال اجباری

FILES = {}  # 🟡 فایل‌ها اینجا ذخیره میشن


# 🔍 چک عضویت
async def is_member(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False


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
        # ❌ اگر عضو نیست
        if not await is_member(bot, user_id):
            keyboard = [
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")]
            ]
            await update.message.reply_text(
                "❌ اول عضو کانال شو بعد دوباره امتحان کن",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return

        # 🚫 بقیه کاربران
        pass


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    # 👑 فقط ادمین می‌تونه فایل بفرسته
    if user_id == ADMIN_ID:
        if update.message.document:
            file_id = update.message.document.file_id
            file_name = update.message.document.file_name or "unknown"
            
            # 💾 ذخیره کد فایل
            FILES[file_name] = file_id
            
            await update.message.reply_text(
                f"✅ فایل ذخیره شد!\n\n"
                f"📝 نام: `{file_name}`\n"
                f"🔑 کد: `{file_id}`\n\n"
                f"⬇️ کد رو کپی کن و توی FILES اضافه کن"
            )
        else:
            await update.message.reply_text("❌ لطفاً فایل بفرست")
    else:
        # ❌ اگر عضو نیست
        if not await is_member(bot, user_id):
            keyboard = [
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")]
            ]
            await update.message.reply_text(
                "❌ اول عضو کانال شو بعد دوباره امتحان کن",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return

        # 🚫 بقیه کاربران - هیچ جواب نمی‌ده
        pass


async def files_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    # 👑 فقط ادمین
    if user_id == ADMIN_ID:
        if not FILES:
            await update.message.reply_text("❌ هیچ فایلی ذخیره نشده")
        else:
            text = "📁 فایل‌های ذخیره شده:\n\n"
            for name, file_id in FILES.items():
                text += f"📝 {name}\n🔑 {file_id}\n\n"
            await update.message.reply_text(text)
    else:
        # ❌ اگر عضو نیست
        if not await is_member(bot, user_id):
            keyboard = [
                [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL.replace('@','')}")]
            ]
            await update.message.reply_text(
                "❌ اول عضو کانال شو بعد دوباره امتحان کن",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return

        pass


async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("files", files_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_message))
    
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
