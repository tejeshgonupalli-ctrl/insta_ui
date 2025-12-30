import re
import requests
from instagrapi import Client
from pathlib import Path


def download_reel_from_url(reel_url, session_file):
    """
    100% SAFE reel downloader
    (does NOT use instagrapi.video_download)

    Returns:
        video_path (str)
        caption (str)
    """

    cl = Client()
    cl.load_settings(session_file)

    # Extract shortcode
    match = re.search(r"/reel/([A-Za-z0-9_-]+)/?", reel_url)
    if not match:
        raise ValueError("Invalid Instagram Reel URL")

    shortcode = match.group(1)

    media_pk = cl.media_pk_from_code(shortcode)
    media = cl.media_info(media_pk)

    video_url = media.video_url
    caption = media.caption_text or ""

    if not video_url:
        raise Exception("Could not fetch video URL")

    output_dir = Path("posts/uploads")
    output_dir.mkdir(parents=True, exist_ok=True)

    video_path = output_dir / f"reel_{shortcode}.mp4"

    # 🔥 MANUAL DOWNLOAD (NO instagrapi bug)
    response = requests.get(video_url, stream=True, timeout=60)
    response.raise_for_status()

    with open(video_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    return str(video_path), caption
