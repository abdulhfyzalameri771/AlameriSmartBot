from telegram import Update
from telegram.ext import ContextTypes

from database import get_user, get_statistics
from config import ADMIN_ID
from handlers.admin import admin_panel, admin_buttons
from keyboards.main_menu import get_main_menu


async def user_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    # أزرار لوحة الإدارة
    admin_menu_buttons = [
        "👥 إدارة المستخدمين",
        "📢 إدارة القنوات",
        "👥 إدارة المجموعات",
        "📣 الإذاعة",
        "🚫 المحظورون",
        "💾 النسخ الاحتياطي",
        "⚙️ الإعدادات",
    ]

    if text in admin_menu_buttons:
        await admin_buttons(update, context)
        return

    if text == "🏠 الرئيسية" or text == "🔙 رجوع":
        await update.message.reply_text(
            "🏠 القائمة الرئيسية",
            reply_markup=get_main_menu()
        )

    elif text == "⚙️ لوحة الإدارة":
        await admin_panel(update, context)

    elif text == "📊 الإحصائيات":

        if update.effective_user.id != ADMIN_ID:
            await update.message.reply_text("⛔ ليس لديك صلاحية.")
            return

        stats = get_statistics()

        await update.message.reply_text(
            f"""📊 إحصائيات البوت

👥 المستخدمون: {stats["users"]}
📢 القنوات: {stats["channels"]}
🚫 المحظورون: {stats["banned"]}"""
        )

    elif text == "👤 حسابي":

        user = get_user(update.effective_user.id)

        username = (
            f"@{user['username']}"
            if user["username"]
            else "لا يوجد"
        )

        await update.message.reply_text(
            f"""👤 معلومات حسابك

🆔 {user["user_id"]}
📛 {username}
📝 {user["full_name"]}
⭐ النقاط: {user["points"]}
👥 الإحالات: {user["referrals"]}"""
        )

    else:
        await update.message.reply_text(
            "اختر زرًا من القائمة."
        )
