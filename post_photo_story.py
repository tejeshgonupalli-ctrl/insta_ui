import sys
from instagrapi import Client

IMAGE_PATH = sys.argv[1]

cl = Client()
cl.load_settings("session_account3.json")

print("✅ Session loaded")

cl.photo_upload_to_story(IMAGE_PATH)

print("🖼️ Photo story uploaded successfully")
