# Used for identify features etc., DO NOT MODIFY
VERSION = "0.4"
# DO NOT MODIFY END

TIME_BETWEEN_CHECK = 10
TIME_BETWEEN_CLEAR = 3600 # An hour
EXPIRY_TIME = 3600 * 6
HTTP_RETRY = 3

BASE_JSON_DIR = "jsons"
LOGS_DIR = "logs"

CHANNELS_JSON = "channels.json"
FETCHED_JSON = "fetched.json"

# Cookie file for login required streams. You can get your cookie with FF or Chrome extensions like "cookies.txt" (Just check https://addons.mozilla.org/ or https://chrome.google.com/webstore/)
COOKIE = None

# Use multi-IPs for checking. One IP per line. Also make sure that each IP is set as individual address on your interface, IP-Ranges dont work.
IP_POOL = None

# Send to discord on video privated
ENABLE_PRIVATE_CHECK = False

# Enable Live stream download
# Replace None with file path e.g. DOWNLOAD = r"H:\DownloadArchive\%(channel)s\%(upload_date)s - %(title)s\%(upload_date)s - %(title)s (%(id)s)"
DOWNLOAD = None
MEMBER_DOWNLOAD = None
PREMIERE_DOWNLOAD = None
PRIVATED_DOWNLOAD = None

# Number of threads for pekopeko's ytarchive-raw-go
PRIVATED_DOWNLOAD_THREADS = 24

# Callbacks
ENABLED_MODULES = {
    "discord": False,
    "telegram": False
}

# If you dont know how to create a Discord webhook read here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
DISCORD_WEBHOOK_URL = None
DISCORD_SEND_FILES = False
DISCORD_TOKEN = None

TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None
TELEGRAM_SEND_FILES = False

# On live
ENABLED_MODULES_ONLIVE = {
    "discord": False,
    "telegram": False,
    "pushalert": False,
    "fcm": False
}

DISCORD_WEBHOOK_URL_ONLIVE = None
DISCORD_WEBHOOK_URL_MEMBERS = None
DISCORD_WEBHOOK_URL_PREMIERE = None

TELEGRAM_BOT_TOKEN_ONLIVE = TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID_ONLIVE = None

PUSHALERT_API_KEY = None
PUSHALERT_ICON = None

FCM_API_KEY = None
FCM_ICON = None
FCM_TARGET = "/topic/all"

# ====== Chat Downloader ====== #
# `pip install chat_downloader`
CHAT_DIR = None

CHAT_INACTIVITY_DURATION = 30
CHAT_BUFFER_TIME = 1
CHAT_TASK_CLEAR_INTERVAL = 300

# `pip install brotlipy`
# `pip install zstandard`
CHAT_COMPRESS = None # None, "brotli", "zstd"
# ====== Chat Downloader END ====== #

CALLBACK_AFTER_EXPIRY = False
CHAT_CALLBACK_AFTER_EXPIRY = False
