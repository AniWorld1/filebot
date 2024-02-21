#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29668491"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "84feb2e86bc3fa3b0b9bc1e3a3428177")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002033286345"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6216046291"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://aniworld:assalom13@cluster0.g12ffko.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "aniworld")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "🎐Assalomu Alaykum Hurmatli{first}\n\n🎐Ushbu bot orqali o'zingizga kerakli bo'lgan fayllarni yuklab olishingiz mumkin!\n🎐Bizning asosiy kanal: @AniFilm_Tv")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6381981989 1637164032").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hurmatli {first}\n\n<b>🎐Botdan to'liq foydalanish uchun ushbu kanllarga qo'shilishingiz kerak!\n\n🎐Kanallarga obuna bo'lgach 'Tasdiqlash' tugmasini bosing!</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Iltimos botga to'g'ridan to'g'ri xabar yubormang! @AniFilm_Tv"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
