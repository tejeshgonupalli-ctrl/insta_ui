import sys
from instagrapi import Client

# Follow cheyyali anna username
TARGET_USERNAME = sys.argv[1]

cl = Client()

# Session load
cl.load_settings("session_account3.json")

print("✅ Session loaded")

# Username → User ID
user_id = cl.user_id_from_username(TARGET_USERNAME)

# ➕ Follow
cl.user_follow(user_id)

print(f"➕ Followed successfully: {TARGET_USERNAME}")
