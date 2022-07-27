import subprocess
import glob
import re
import argparse


argpar = argparse.ArgumentParser(
    prog="dropkick-on-my-devil-x-downloader",
    usage="https://github.com/fa0311/dropkick-on-my-devil-x-downloader",
    description="dropkick on my devil x downloader",
)
argpar.add_argument("-o", "--output", default="output.mp4")
argpar.add_argument("--url", default="PLStlXMBhWF_RWMSuq-4sbDEDLCXLxWNEy")
argpar.add_argument("--ffmpeg-path", default="ffmpeg")
argpar.add_argument("--youtubedl-path", default="yt-dlp")


arg = argpar.parse_args()

process = subprocess.Popen(
    [arg.youtubedl_path, arg.url, "-o", "temp\%(title)s"],
    shell=True,
    stdout=subprocess.PIPE,
)
for line in process.stdout:
    text = line.decode("shift-jis").strip()
    print(text)

files = glob.glob("temp/*")
sorted = sorted(
    files, key=lambda x: int(re.findall("\[([0-9]+)_[0-9]+\]", x)[0]), reverse=False
)
playlist = ""
for file in sorted:
    playlist += "file {0}\n".format(file.replace("\\", "/"))
with open("playlist.txt", mode="w", encoding="utf-8") as f:
    f.write(playlist)

process = subprocess.Popen(
    [
        arg.ffmpeg_path,
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        "playlist.txt",
        "-c",
        "copy",
        arg.output,
    ],
    shell=True,
    stdout=subprocess.PIPE,
)
for line in process.stdout:
    text = line.decode("shift-jis").strip()
    print(text)
