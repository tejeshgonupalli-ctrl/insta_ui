import os
import subprocess

def add_story_watermark(video_path, watermark_text=None):
    if not os.path.exists(video_path):
        raise FileNotFoundError(video_path)

    watermark_img = "watermark.png"
    if not os.path.exists(watermark_img):
        raise FileNotFoundError("watermark.png not found in project root")

    output_path = video_path.replace(".mp4", "_wm.mp4")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", watermark_img,
        "-filter_complex",
        "[0:v][1:v]overlay=20:20:format=auto",
        "-map", "0:v:0",
        "-map", "0:a:0",
        "-c:v", "libx264",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        output_path
    ]

    subprocess.run(cmd, check=True)
    return output_path

