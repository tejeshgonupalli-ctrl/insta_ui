import sys
from instagrapi import Client
from caption_hashtag import generate_caption, generate_hashtags
from watermark_video import add_watermark


INPUT_VIDEO = sys.argv[1]
USERNAME = sys.argv[2]

OUTPUT_VIDEO = "final_reel.mp4"

# 1️⃣ Watermark add
add_watermark(INPUT_VIDEO, OUTPUT_VIDEO, USERNAME)

# 2️⃣ Caption + Hashtags
caption = generate_caption(USERNAME)
hashtags = generate_hashtags()
final_caption = caption + "\n\n" + hashtags

# 3️⃣ Instagram upload
cl = Client()
cl.load_settings("session_account3.json")

print("✅ Session loaded")

cl.video_upload(
    OUTPUT_VIDEO,
    caption=final_caption
)

print("🎬 Reel uploaded with caption + hashtags + watermark")
