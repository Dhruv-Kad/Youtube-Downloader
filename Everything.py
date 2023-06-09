import sys

from moviepy.editor import *
from pytube import YouTube
import os
def dl(type, Link):
    if type == 1:
        z = Download.AudioOnly("Goodluck", Link, jpath)
        print(z)
        mp4_path = jpath + "/" + z
        mp3file = jpath + "/" + "AUDIOONLY" + z + ".mp3"
        videoClip = VideoFileClip(mp4_path)
        audioclip = videoClip.audio
        audioclip.write_audiofile(mp3file)
        os.remove(mp4_path)
    else:
        Download.Normal("Pass", Link, jpath)
class Download:
    def __init__(self):
        pass
    def AudioOnly(self, link, PATH):
        yt = YouTube(link,use_oauth=True, allow_oauth_cache=True)
        au = yt.streams.get_lowest_resolution()
        au.download(PATH)
        return yt.streams.get_lowest_resolution().default_filename
    def Normal(self, link, PATH):
        yt = YouTube(link,use_oauth=True, allow_oauth_cache=True)
        ad = yt.streams.get_highest_resolution()
        ad.download(PATH)
stop = 0
name_strings = []
while stop != 1:
    jpath = ""
    tempjpath = ""
    firstime = True
    try:
        fh = open('Path.txt', 'r')
        jpath = str(fh.read())
    except FileNotFoundError:
        print("First time user? :D")

    type = input("Enter 1 for audio only, zero for a normal download: ")
    rawinput = input("Enter the link(s) in here(if links = >1 use one comma to seperate them ex;link,link1: ")
    if ',' in rawinput:
        allsame = input("Type 1 if you would like for all formats in the list to be the same: ")
        split_strings = [s.strip() for s in rawinput.split(',')]
        for s in split_strings:
            yd = YouTube(s, use_oauth=True, allow_oauth_cache=True)
            name_strings.append(yd.title)
        print(split_strings)
        print(name_strings)

        for i in split_strings:
            yv = YouTube(i, use_oauth=True, allow_oauth_cache=True)
            name = yv.title
            if allsame != 1:
                type = input("Enter 1 for audio only, zero for a normal download for " + name +" : ")
            dl(type,i)
    else:
        yd = YouTube(rawinput, use_oauth=True, allow_oauth_cache=True)
        print(yd.title)
        dl(type,rawinput)
    stop = int(input("type 1 to stop: "))

if(stop == 1):
    sys.exit()



