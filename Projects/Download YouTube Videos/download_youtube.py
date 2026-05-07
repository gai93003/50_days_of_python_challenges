from yt_dlp import DownloadError, YoutubeDL


VIDEO_URL = "https://www.youtube.com/shorts/AhkbzMOQoIA"
OUTPUT_DIR = "/home/gabriel/Desktop"


ydl_opts = {
	# Prefer MP4 around 360p; fallback to the best available if exact match is missing.
	"format": "best[ext=mp4][height<=360]/best[height<=360]/best[ext=mp4]/best",
	"outtmpl": f"{OUTPUT_DIR}/%(title)s.%(ext)s",
	"noplaylist": True,
}


try:
	with YoutubeDL(ydl_opts) as ydl:
		ydl.download([VIDEO_URL])
except DownloadError as error:
	  print(f"Download failed: {error}")