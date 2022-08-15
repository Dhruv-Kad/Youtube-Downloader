from pytube import YouTube

class Download:
    def __init__(self):
        pass
    def AudioOnly(self, link):
        yt = YouTube(link)
        print(yt.title)
        au = yt.streams.get_audio_only()
        au.download("D:\YT VIDEOS")
    def Normal(self, link):
        yt = YouTube(link)
        print(yt.title)
        print(yt.views)
        ad = yt.streams.get_highest_resolution()
        ad.download("D:\YT VIDEOS")


