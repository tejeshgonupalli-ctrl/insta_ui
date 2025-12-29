import sys
from instagrapi import Client

USERNAME = sys.argv[1]   # receiver instagram username
MESSAGE = sys.argv[2]    # message text

cl = Client()

# Session load
cl.load_settings("session_account5.json")

print("✅ Session loaded")

# User ID get cheyyadam
user_id = cl.user_id_from_username(USERNAME)

# DM send
cl.direct_send(MESSAGE, [user_id])

print("💬 DM sent successfully")
