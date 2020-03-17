import pytube
import os
from moviepy.editor import *

video_url = input("Write the youtube video url: ")

youtube = pytube.YouTube(video_url)
video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().last()
title = video.download(filename='tmp')
os.chmod(title, 777)

video = VideoFileClip(title)
video.audio.write_audiofile(os.path.join(os.getcwd(), "music.mp3"))
os.remove(title)
