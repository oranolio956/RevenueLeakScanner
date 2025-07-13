import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7771821977:AAGdkEXXtE_iNLCtvF8qDY_SZnUgABeWMhA"  # Use your actual token as a string or use os.getenv("TG_TOKEN")
CHANNEL_ID = -1002537810913
CHANNEL_USER = "ofmdoneright"
APP_LINK = "https://revenueleakscanner-fftpwdjeswbtckg7zgaruu.streamlit.app/"

def join_button():
    url = f"https://t.me/{CHANNEL_USER}"
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔗 Join Channel", url=url)]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ("member", "administrator", "creator"):
            await update.message.reply_text(
                f"Here’s your scanner link – happy hunting!\n{APP_LINK}"
            )
        else:
            await update.message.reply_text(
                "Please join our channel to unlock the free tool.",
                reply_markup=join_button()
            )
    except Exception:
        await update.message.reply_text(
            "Please join our channel to unlock the free tool.",
            reply_markup=join_button()
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Upload your OnlyFans CSV (subscriptions, PPV, tips) to the scanner after joining the channel. "
        "You must have the right to use the data. For format help, see the README."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
