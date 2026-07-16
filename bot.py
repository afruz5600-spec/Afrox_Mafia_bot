import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Loggingni sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Salom {user.mention_html()}!\nMen GitHub-ga yuklash uchun tayyorlangan botman."
    )

# /help komandasi uchun funksiya
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Yordam: Menga xabar yuboring, men uni qaytaraman.")

# Xabarlarni qaytarish funksiyasi
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text:
        await update.message.reply_text(update.message.text)

# Xatoliklarni ushlash funksiyasi
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Xatolik yuz berdi: {context.error}")

def main() -> None:
    # Tokenni o'rniga qo'yamiz
    TOKEN = "8937651791:AAFGvGTx4K8G0jOtZ5FbucnmIzmki2CfeeY"
    
    # Application yaratish
    application = Application.builder().token(TOKEN).build()

    # Handlerlarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Xatolikni boshqarish
    application.add_error_handler(error_handler)

    # Botni ishga tushirish
    print("Bot ishga tushdi...")
    application.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
