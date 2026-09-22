import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID", "6471551604"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏏 ODI", callback_data='odi'), InlineKeyboardButton("🏏 TEST", callback_data='test')],
        [InlineKeyboardButton("⚽ Football", callback_data='football'), InlineKeyboardButton("🎾 Tennis", callback_data='tennis')]
    ]
    await update.message.reply_text(
        "Welcome to Ball Guy Bot! Select sport:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text(f"✅ {q.data.upper()} alerts ON!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()

if __name__ == "__main__":
    main()
