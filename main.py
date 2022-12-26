import threading
from tkinter.messagebox import showerror, showwarning

from Tools.scripts.combinerefs import combine
from pytube import Playlist

from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Youtube Playlist Downloader")
input_variable = StringVar()


def audio():
    if input_variable.get() == "":
        showwarning('No playlist detected', 'Please add a playlist url')
    else:
        p = Playlist(input_variable.get())
    lbl2 = Label(root, text=f'Downloading: {p.title}', fg="blue", width=80, font="courrier")
    lbl2.place(x=100, y=300)
    for video in p.videos:
        print(video.title)
        st = video.streams.get_highest_resolution()
        st.download()
        # video.streams.first().download()


def sel():
    selection = str(var.get())
    print(selection)


var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                 command=sel)
R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                 command=sel)
R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                 command=sel)
stop_event = threading.Event()


def video():
    if input_variable.get() == "":
        showwarning('No playlist detected', 'Please add a playlist url')
    else:
        p = Playlist(input_variable.get())
        lbl2 = Label(root, text=f'Downloading: {p.title}', fg="blue", width=70, font="courrier")
        lbl2.place(x=100, y=250)
    for video in p.videos:
        print(video.title)
        st = video.streams.get_highest_resolution()
        st.download()
        # video.streams.first().download()


entry1 = Entry(root, fg="blue", textvariable=input_variable, width=80)
lbl1 = Label(root, text="Enter playlist URL", fg="blue", font="courrier")
lbl1.place(x=120, y=50)
button = Button(root, text="Download Audios", command=threading.Thread(target=audio).start, bg="cyan4", fg="white",
                font="courrier")
button1 = Button(root, text="Download Videos", command=threading.Thread(target=video).start, bg="cyan4", fg="white",
                 font="courrier")
entry1.place(x=100, y=100)
button.place(x=300, y=200)
button1.place(x=100, y=200)
root.mainloop()
