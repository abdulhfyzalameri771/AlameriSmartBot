import logging

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import BOT_TOKEN
from database import init_db
from handlers.start import start
from handlers.user import user_buttons
from handlers.admin import admin_buttons, stats_callback, channels_callback


logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting Alameri Smart Bot...")

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CallbackQueryHandler(stats_callback, pattern="^stats$"))
    app.add_handler(CallbackQueryHandler(channels_callback, pattern="^channels$"))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            admin_buttons,
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            user_buttons,
        )
    )

    logger.info("Bot is running...")

    app.run_polling(
        allowed_updates=[
            "message",
            "callback_query",
            "chat_member",
        ]
    )


if __name__ == "__main__":
    main()
