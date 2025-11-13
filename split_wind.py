import os
import subprocess

INPUT_DIR = "dataset/background/wind"
OUTPUT_DIR = "dataset/background/wind_5sec"
SEGMENT_TIME = "5"  # seconds

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.lower().endswith((".mp3", ".wav")):
        in_path = os.path.join(INPUT_DIR, file)

        base = os.path.splitext(file)[0].replace(" ", "_")
        out_pattern = os.path.join(OUTPUT_DIR, base + "_%03d.wav")

        print(f"Processing: {in_path}")

        cmd = [
            "ffmpeg",
            "-y",
            "-i", in_path,
            "-ac", "1",          # mono
            "-ar", "32000",      # 32 kHz
            "-f", "segment",
            "-segment_time", SEGMENT_TIME,
            out_pattern
        ]

        subprocess.run(cmd)
