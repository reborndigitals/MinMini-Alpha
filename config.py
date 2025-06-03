import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29650844")) #optional
API_HASH = getenv("API_HASH", "6154d581d370cbdadd240292c456d7a2") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1281282633 8187361583 7888151947 7948585276").split()))
OWNER_ID = int(getenv("OWNER_ID", "1281282633"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://iamnobita1:nobitamusic1@cluster0.k08op.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "2132260441:AAEGAiQWe8lq-O6IvoWoY-4BROsoqxiPc-E")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/9ee37cccd7bf55c3ec953.png')
ALIVE_TEXT = getenv("ALIVE_TEXT", "ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙᴇ..🏓 \n\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❤️ \n[𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖‌֯֟፝‌𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞‌֟֠֯፝‌𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘▹ᴴᴮ⸳⸳ⷮ⸳⸳ⷨ](https://t.me/HeartBeat_Muzic)")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001735663878")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://t.me/HeartBeat_Muzic")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQHEb5wAdTujpFz8ZlEEOtmho5Fl2rI58BbimhjFXZdFfBGg3le1JX7vBy5H7afdoHWMUIhG_1A1b9gz-soB86Xyy-WGWxRHPdckCDVCWi33Kdc7ykGCEhx6WvbgTIQH_iEXshe6rfa0Soj99QXuEseQKewFFybW3HogO-R8l82-wInIHWNcQFy0sVTb-2JwTRjl4RlgVCp7SILmcNFQx4o7m1UpKDcmuqAyvbwO5q7FubdESrc_9SLp3OGv6taJC6tTdajkVPDHJaLUHsVQwv4hhh0LyAqmImJREdA6Th73WqwhJN9bJp_ovrSIabiDk1mlnrDWKiGthczV02aPI-3lRtmHOgAAAAHHZ9BxAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
