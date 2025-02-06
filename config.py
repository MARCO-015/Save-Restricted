# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21771444"))
API_HASH = getenv("API_HASH", "4162cac0a1a3e792023b8e9092030d8c")
BOT_TOKEN = getenv("BOT_TOKEN", "7784502607:AAFd5S3PFFTep5I8a8CAjzPFTrdKt8T7RYI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7548265642").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Test2:Monstersir123@cluster0.ltadb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002275877038")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002341507214"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "5cc622e06b9f408dca33e939b2864329eb39621e")
STRING = getenv("STRING", "BQFMNLQAagvLgKI259M8uDfowgRhhGJqI-bzbJv1_k4t_as63uzi5XnVi0aio0r4B-pOdHWFyIB0q6hYX1SszgUgjz7zHPFdVZl_F5vjc5eSEUdKwnIE-Upf8WzvZg4swTlqIihzPKbJSmlV3rA1gduJ2fBzK-SCzGxgTf3xpHkhTMcEw1QGfAnJkYQ5DiHmGsLjumi4V56ZBKjYWZWmIAJbNzeQeiRhjPijWYl-AThFcDrVeJb_pUbRkMT0uUXO6Rw0OtvcwaJ-Njc_CwbSsEras7pOEtg_N9y8P-J8KeVGPoEqOZZvbHqpEMGypkVXF9lX5WUzhvC0yDpt95doSWtMaovjkQAAAAGIiOaNAA")
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
