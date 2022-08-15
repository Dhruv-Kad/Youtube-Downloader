import PySimpleGUI as sg
from main import Download
type = ""
layout = [
    [sg.InputText("Input link")],
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
    #Passes link and type outside of loop
    Link = str(values[0])
    type = event
    break
window.close()
#Checks link and type
print(Link)
print(type)
#Runs Audio only vs Full download
if type == "Audio Only":
    Download.AudioOnly("Goodluck", Link)
else:
    Download.Normal("Pass", Link)


