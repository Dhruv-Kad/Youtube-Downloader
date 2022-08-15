from pytube import YouTube
import PySimpleGUI as sg

class Download:
    def __init__(self):
        pass
    def AudioOnly(self, link, PATH):
        yt = YouTube(link)
        print(yt.title)
        au = yt.streams.get_audio_only()
        au.download(PATH)
    def Normal(self, link, PATH):
        yt = YouTube(link)
        print(yt.title)
        print(yt.views)
        ad = yt.streams.get_highest_resolution()
        ad.download(PATH)

jpath = ""
tempjpath = ""
firstime = True
try:
    fh = open('Path.txt', 'r')
    jpath = str(fh.read())
except FileNotFoundError:
    print("First time user? :D")

type = ""
layout = [
    [sg.InputText("Input link")],
    [sg.Txt("Put the path to the folder you want your downloads to be in:"), sg.InputText(jpath)],
    [sg.Button("Audio Only"), sg.Button("Normal")]
]
Link = ""
#Creates popup
window = sg.Window('Youtube-Downloader', layout)
#main loop
while True:
    #Reads all events and values passed in gui
    event, values = window.read()
    #CLOSING FUNC
    if event == sg.WINDOW_CLOSED:
        break
        quit()
    #Passes link and type outside of loop
    Link = str(values[0])
    type = event
    tempjpath = str(values[1])
    break
window.close()
try:
    fh = open('Path.txt', 'r')
except FileNotFoundError:
    print("File not found,creating new path")
    with open('Path.txt', 'w') as f:
        f.write(tempjpath)
        jpath = tempjpath
#Checks link and type
print(Link)
print(type)


#Runs Audio only vs Full download
if type == "Audio Only":
    Download.AudioOnly("Goodluck", Link, jpath)
else:
    Download.Normal("Pass", Link, jpath)
#"D:\YT VIDEOS"

