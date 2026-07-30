from telegram import ReplyKeyboardMarkup


def get_admin_menu():
    keyboard = [
        ["📢 إدارة القنوات", "👥 إدارة المستخدمين"],
        ["👥 إدارة المجموعات", "📊 الإحصائيات"],
        ["📣 الإذاعة", "🎁 المكافآت"],
        ["🚫 المحظورون", "💾 النسخ الاحتياطي"],
        ["⚙️ الإعدادات"],
        ["🔙 رجوع"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True,
    )


def get_channels_menu():
    keyboard = [
        ["➕ إضافة قناة"],
        ["📋 عرض القنوات"],
        ["❌ حذف قناة"],
        ["🔙 رجوع"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True,
    )
