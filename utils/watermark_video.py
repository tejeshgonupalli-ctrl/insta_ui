import os
import subprocess
import uuid

def add_story_watermark(video_path, watermark_text="@test_audio"):
    if not os.path.exists(video_path):
        raise FileNotFoundError(video_path)

    output_path = video_path.replace(".mp4", "_wm.mp4")
    ass_path = f"temp_{uuid.uuid4().hex}.ass"

    # Create ASS subtitle file
    ass_content = f"""
[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Watermark,Arial,48,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,3,1,2,30,30,50,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,9:59:59.00,Watermark,,0,0,0,,{watermark_text}
"""

    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vf", f"ass={ass_path}",
        "-c:v", "libx264",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        output_path
    ]

    subprocess.run(cmd, check=True)

    os.remove(ass_path)
    return output_path
