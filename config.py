from dotenv import load_dotenv
import os

# تحميل متغيرات البيئة
load_dotenv()

# بيانات البوت
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# معرف المالك
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# قاعدة البيانات
DATABASE_NAME = os.getenv("DATABASE_NAME")

# السجل
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
