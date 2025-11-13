import os
import subprocess

INPUT_ROOT = "Drone types"
OUTPUT_ROOT = "dataset/drone"
SEGMENT_TIME = "5"  # seconds

os.makedirs(OUTPUT_ROOT, exist_ok=True)

for drone_folder in os.listdir(INPUT_ROOT):
    in_dir = os.path.join(INPUT_ROOT, drone_folder)
    if not os.path.isdir(in_dir):
        continue

    # Output folder name: replace spaces with underscores
    out_dir_name = drone_folder.replace(" ", "_")
    out_dir = os.path.join(OUTPUT_ROOT, out_dir_name)
    os.makedirs(out_dir, exist_ok=True)

    for fname in os.listdir(in_dir):
        if not fname.lower().endswith(".wav"):
            continue

        in_path = os.path.join(in_dir, fname)
        out_pattern = os.path.join(out_dir, out_dir_name + "_%03d.wav")

        print(f"Splitting {in_path} -> {out_pattern}")

        cmd = [
            "ffmpeg",
            "-y",
            "-i", in_path,
            "-ac", "1",
            "-ar", "32000",
            "-f", "segment",
            "-segment_time", SEGMENT_TIME,
            out_pattern,
        ]

        subprocess.run(cmd)
