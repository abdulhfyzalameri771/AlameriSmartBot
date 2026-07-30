from database import get_statistics
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


def admin_buttons():
    keyboard = [
        [InlineKeyboardButton("📊 الإحصائيات", callback_data="stats")],
        [InlineKeyboardButton("📢 إدارة القنوات", callback_data="channels")],
    ]

    return InlineKeyboardMarkup(keyboard)

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔧 لوحة الإدارة",
        reply_markup=admin_buttons()
    )
async def stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    stats = get_statistics()

    text = (
        "📊 الإحصائيات\n\n"
        f"👤 عدد المستخدمين: {stats['users']}\n"
        f"📢 عدد القنوات: {stats['channels']}"
    )

    await query.edit_message_text(text)

async def channels_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "📢 إدارة القنوات\n\n"
        "هذه الصفحة ستكون خاصة بإدارة القنوات."
    )
