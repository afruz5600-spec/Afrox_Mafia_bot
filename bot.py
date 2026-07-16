import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Loggingni sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot muvaffaqiyatli ishga tushdi.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    # Tokenni shu yerga qo'ying
    TOKEN = "8937651791:AAFGvGTx4K8G0jOtZ5FbucnmIzmki2CfeeY"
    
    # ApplicationBuilder ishlatish eng xavfsiz yo'l
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handlerlarni qo'shish
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    # Botni ishga tushirish
    print("Bot ishlamoqda...")
    application.run_polling()
