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
STRING = getenv("STRING", "BQFMNLQACcFAhNnzFS1Ut5PSamRk2B6iNtGaD4nQ9Mc9r_u_4GotAqmVtwHlLO3QHud7feI6T8xPZNxB8B78_L-PWvA61w0cBp_GX9bZS9IYMP4G3rm1mJc0YnJKFb5pDCalufRYNGnrk6W4S1yvTaWBmVn29StqiKWIxGDtF0_8Zx0b36CGlr0wDLZCXSImSC0l_cTq_-J3SS7uQTQyE7PmyJezgyNBvQPHG5KJZBOR7X5uV4Z2dZhCxCKHy0o5GuWzJGWtjP7widuwheyHhL6b4gDu8jLHXO2wSY5F7PtP6HciOLX8iBdAVKiMeVHo3I2hKz2QnH_MMNZHalNlFP3fyWPOTAAAAAGIiOaNAA")
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
