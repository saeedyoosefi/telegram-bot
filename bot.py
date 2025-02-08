from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# 🔹 توکن دریافتی از BotFather را اینجا بذار
TOKEN = "7680196420:AAHYs39TnQzTz9G_jqO0Po83bJG9Uxc1HrA"

# 🔹 تابعی که هنگام ارسال /start اجرا می‌شود
async def start(update: Update, context) -> None:
    await update.message.reply_text("سلام! من ربات تلگرام هستم. دستورات رو امتحان کن.")

# 🔹 تابعی که پیام‌های کاربران رو دریافت و همان را برمی‌گرداند
async def echo(update: Update, context) -> None:
    await update.message.reply_text(update.message.text)

# 🔹 راه‌اندازی ربات
def main():
    app = Application.builder().token(TOKEN).build()

    # 🔹 تعریف دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 🔹 اجرای ربات
    print("✅ ربات روشن شد! منتظر پیام‌های تلگرام هستم...")
    app.run_polling()

if __name__ == "__main__":
    main()
