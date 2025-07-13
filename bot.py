import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ── CONFIG ────────────────────────────────────────────────────────────
TOKEN        = os.getenv("TG_TOKEN", "7771821977:AAGdkEXXtE_iNLCtvF8qDY_SZnUgABeWMhA")
CHANNEL_ID   = int(os.getenv("CHANNEL_ID", "-1002537810913"))   # numeric
CHANNEL_USER = os.getenv("CHANNEL_USER", "ofmdoneright") # no @
APP_LINK     = os.getenv("APP_LINK", "https://revenueleakscanner-fftpwdjeswbtckg7zgaruu.streamlit.app/")

# ── HELPERS ───────────────────────────────────────────────────────────
def join_button() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔗 Join Channel", url=f"https://t.me/{CHANNEL_USER}")]]
    )

# ── HANDLERS ──────────────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ("member", "administrator", "creator"):
            await update.message.reply_text(
                "Welcome to ApexFind—where data science dismantles guesswork.\n\n"
                f"Here’s your scanner link – happy hunting!\n{APP_LINK}"
            )
        else:
            await update.message.reply_text(
                "🚀 Please join our channel to unlock the free tool.",
                reply_markup=join_button()
            )
    except Exception:
        await update.message.reply_text(
            "🚀 Please join our channel to unlock the free tool.",
            reply_markup=join_button()
        )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Upload your OnlyFans CSV (subscriptions, PPV, tips) after joining the channel.\n"
        "Required columns: fan_id, date, revenue, type."
    )

# ── MAIN ──────────────────────────────────────────────────────────────
def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    print("Telegram bot online …")
    app.run_polling()

if __name__ == "__main__":
    main()
