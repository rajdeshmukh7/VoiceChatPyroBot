# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2452280
API_HASH = "6c553a78aca54e22a50d2f4288cc118b"

# Get this from @Botfather
TOKEN = "1569679360:AAGqwvCLTH7DC4a8LN9h3RuKgcRTXf0Sg9s"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1032532939,
    814563017,
    928211812,
    1130863968,
    726344075,
    933022304,
    1012876560,
    622063078,
    978279098,
    1007750321,
    1318286335,
    757223254,
    1067188884,
    1356307212,
    748150648,
    719195224,
    666365184,
]

# The ID of the group where your bot streams
GROUP = -1001336628696

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Send "now playing" messages to the group
LOG = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 180

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
