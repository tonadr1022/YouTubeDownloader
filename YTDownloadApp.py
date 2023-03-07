# conda activate ytenv
from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import datetime

file_extention = ''
adaptive = True


def setParameters():
    pass


def setVideo():
    yt = YouTube('https://www.youtube.com/watch?v=0iUAdKk_8V0')
    print(yt)
    return yt


def downloadFile():
    yt = setVideo()
    print(yt.streams.filter(type='video'))
    video = yt.streams.get_lowest_resolution()
    print(video)
    # video.download()


def printInfo():
    yt = setVideo()
    minutes = int(yt.length) // 60
    seconds = int(yt.length) - int(minutes*60)
    lengthStr = str(minutes) + ":" + str(seconds)
    date = str(yt.publish_date)[:11]
    titleText.set("Title: " + yt.title)
    channelText.set("Channel Name: " + yt.author)
    dateText.set('Publish Date: ' + date)
    lengthText.set('Length: ' + lengthStr)
    viewsText.set('Number of Views: ' + str(yt.views))


# downloadFile()

root = tk.Tk()
root.title('YouTube Video Downloader')
root.geometry('1200x500')

style = ttk.Style(root)
style.configure('my.TLabel', font=('Comic Sans MS', 20))

mainCommandFrame = ttk.Frame(root)
mainCommandFrame.pack(anchor='center', expand=True)


linkLabel = ttk.Label(mainCommandFrame, text="Enter a link", style='my.TLabel')
linkLabel.grid(row=0, column=0)
linkEntry = ttk.Entry(mainCommandFrame, width=40)
linkEntry.grid(row=1, column=0)
buttonFrame = ttk.Frame(mainCommandFrame)
buttonFrame.grid(row=2, column=0)
infoButton = ttk.Button(buttonFrame, text="Get Info", command=printInfo)
infoButton.grid(row=0, column=0, padx=20)
downloadButton = ttk.Button(
    buttonFrame, text="Download", command=downloadFile)
downloadButton.grid(row=0, column=1, padx=20)

infoFrame = ttk.Frame(root)
infoFrame.pack(anchor='center', expand=True)
titleText = tk.StringVar()
titleText.set("Title: ")
titleLabel = ttk.Label(infoFrame, textvariable=titleText, style='my.TLabel')
titleLabel.grid(row=0, column=0, sticky='w')
channelText = tk.StringVar()
channelText.set("Channel Name: ")
channelLabel = ttk.Label(
    infoFrame, textvariable=channelText, style='my.TLabel')
channelLabel.grid(row=1, column=0, sticky='w')
dateText = tk.StringVar()
dateText.set('Publish Date: ')
dateLabel = ttk.Label(infoFrame, textvariable=dateText, style='my.TLabel')
dateLabel.grid(row=2, column=0, sticky='w')
lengthText = tk.StringVar()
lengthText.set('Length: ')
lengthLabel = ttk.Label(infoFrame, textvariable=lengthText, style='my.TLabel')
lengthLabel.grid(row=3, column=0, sticky='w')
viewsText = tk.StringVar()
viewsText.set('Number of Views: ')
viewsLabel = ttk.Label(infoFrame, textvariable=viewsText, style='my.TLabel')
viewsLabel.grid(row=4, column=0, sticky='w')


root.mainloop()

# [<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
# <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">,
# <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">


# validate by printing title, thumbnail
# progress bar
# select quality
# select audio only or not
#
