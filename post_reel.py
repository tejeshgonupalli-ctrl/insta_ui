import sys
from instagrapi import Client

# Command line nundi video path
VIDEO_PATH = sys.argv[1]

# Caption optional
CAPTION = sys.argv[2] if len(sys.argv) > 2 else "Reposted 🔁"

# Client create
cl = Client()

# Session load (already login ayina account)
cl.load_settings("session_account3.json")

print("✅ Session loaded")

# 🔁 Reel upload
cl.video_upload(
    VIDEO_PATH,
    caption=CAPTION
)

print("🎬 Reel uploaded successfully")
