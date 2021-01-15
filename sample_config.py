# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 979327
API_HASH = "b057c9ebd6c629144d28790e6e476735"

# Get this from @Botfather
TOKEN = "1569679360:AAGqwvCLTH7DC4a8LN9h3RuKgcRTXf0Sg9s"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1032532939,
    814563017,
    928211812
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
DUR_LIMIT = 120

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
