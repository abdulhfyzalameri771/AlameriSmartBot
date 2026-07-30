from telegram import ReplyKeyboardMarkup

def get_main_menu():
    keyboard = [
        ["🏠 الرئيسية"],
        ["📢 قنواتي", "👥 مجموعاتي"],
        ["📊 الإحصائيات", "🎁 المكافآت"],
        ["🎯 المهام اليومية", "👤 حسابي"],
        ["⚙️ لوحة الإدارة", "❓ المساعدة"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True
    )
