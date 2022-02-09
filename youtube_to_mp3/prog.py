import os
import youtube_dl

from moviepy.editor import VideoFileClip

video_title = "tmp"

ydl_opts = {
    'outtmpl': os.path.join(os.getcwd(), video_title),
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([input("Write the youtube video url: ")])

os.chmod(video_title, 777)
video = VideoFileClip(video_title)
video.audio.write_audiofile(os.path.join(os.getcwd(), "music.mp3"))
os.remove(video_title)
