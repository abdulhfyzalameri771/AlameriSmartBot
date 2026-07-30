from telegram import Update
from telegram.ext import ContextTypes

from database import add_user, update_last_seen
from keyboards.main_menu import get_main_menu
from config import ADMIN_ID

from handlers.admin import admin_panel


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(
        user.id,
        user.username,
        user.full_name,
    )

    update_last_seen(user.id)

    if user.id == ADMIN_ID:
        await admin_panel(update, context)
        return

    await update.message.reply_text(
        f"👋 أهلاً بك {user.first_name}\n\n"
        "مرحبًا بك في Alameri Smart Bot",
        reply_markup=get_main_menu(),
    )
