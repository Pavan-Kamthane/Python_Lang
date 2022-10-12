# importing module
import youtube_dl
from bs4 import BeautifulSoup
import requests
from tkinter import *
import tkinter.ttk as ttk


# defining functions

# function to download the video
def downloadvideo():
    link_of_the_video = video_link_entry.get()
    link = link_of_the_video.strip()
    ydl_opts = {
        'outtmpl': r"C:/Users/rsrs/YouTube/%(title)s.%(ext)s",
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    # getting the title of the video
    req = requests.get(link)
    s = BeautifulSoup(req.text, "html.parser")
    title = s.find("title")
    title_2 = title.string.replace("<title>", " ")
    title_3 = title_2.replace(" - YouTube", "")
    video_title = Label(gui, text="Video Title: " + title_3, font="arial 8 bold", foreground="Black",
                        background="light cyan")
    video_title.place(x=100, y=160)


# print("Title: ",title_3)
# print("File location: ",r"C:\Users\rsrs\YouTube")

# function called after the video is downloaded to change the labels
def after_download_msg():
    video_link.destroy()
    video_link_entry.destroy()
    button1.destroy()
    download_msg.place(x=100, y=100)
    path_msg.place(x=100, y=130)


# my_hook determines the progress of the download
def my_hook(d):
    if d['status'] == 'finished':
        after_download_msg()
        print("Done downloading")
    if d['status'] == 'downloading':
        gui.update_idletasks()
        pb1['value'] = float(str(d['_percent_str']).replace("%", ""))
    # print(d['filename'], d['_percent_str'], d['_eta_str'])


# main code

# creating gui window
gui = Tk()
gui.geometry("500x500")
gui.config(background="PeachPuff2")
gui.resizable(width=True, height=True)
gui.title('YouTube Video Downloader')
# making labels, entry box and button
video_link = Label(gui, text="Copy & paste the URL of the YouTube video you want to download:- ", font="arial 8 bold", foreground="Black", background="floral white")
video_link.place(x=60, y=50)
video_link_entry = Entry(gui, background="SkyBlue2", width=62)
video_link_entry.place(x=60, y=100)
button1 = Button(gui, text="Enter", bg="white", command=lambda: downloadvideo(), height=1, width=7, relief=GROOVE)
button1.place(x=195, y=150)
download_msg = Label(gui, text="Your video has been downloaded and is in the folder", font="arial 8 bold", foreground="Black", background="light cyan")
path_msg = Label(gui, text=r"C:\Users\rsrs\YouTube", font="arial 8 bold", foreground="Black", background="light cyan")
# making the progress bar which takes the progress updates from the my_hook function
pb1 = ttk.Progressbar(gui, orient=HORIZONTAL, length=300, mode='indeterminate')
pb1.grid(padx=100, pady=200)

gui.mainloop()
