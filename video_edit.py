from audioop import reverse
from moviepy.editor import *
from moviepy.video.fx.all import crop
import os

def cropping(video_name, width_diff=60, height_diff=100):
    if video_name not in os.listdir("cropped_tiktoks"):
        clip = VideoFileClip("tiktoks/"+video_name)
        width, height = int(clip.w), int(clip.h)
        print(width, height)
        clip1 = crop(clip, x1=width_diff, x2=width-width_diff, y1=height_diff, y2=height-height_diff)
        clip1.write_videofile("cropped_tiktoks/"+video_name)
    else:
        print(f"{video_name} is already cropped!")

def get_audio(video_name):
    if video_name[:-4]+".mp3" not in os.listdir("audio"):
        audio1 = VideoFileClip("cropped_tiktoks/"+video_name).audio
        audio1.write_audiofile("audio/"+video_name[:-4]+".mp3")
    else:
        print(f"{video_name}'s audio is already downloaded!")

def put_audio(video_name, audio_name):
    video_clip = VideoFileClip("cropped_tiktoks/"+video_name)
    audio_clip = AudioFileClip("audio/"+audio_name)
    new_name = video_name[:-4]+"-"+audio_name[:-4] +".mp4"
    if new_name not in os.listdir("final_video"):
        final_video = video_clip.set_audio(audio_clip)
        final_video.write_videofile("final_video/"+new_name)
    else:
        print(f"File with {new_name} already exists!")


for video in os.listdir("tiktoks"):
    cropping(video)
    get_audio(video)

audios = os.listdir("audio")
videos = os.listdir("cropped_tiktoks")
audios.reverse()
if len(audios) == len(videos):
    for i in range(len(videos)):
        put_audio(videos[i], audios[i])
else:
    raise ValueError("Length of audios and videos aren't matched!")