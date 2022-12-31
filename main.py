import os
import PySimpleGUI as sg
import youtube_dl
import threading




# Download function
def download(ydl_opts, url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Show a success message
    sg.popup("Playlist downloaded!")
# Set up the UI layout
layout = [
    [sg.Text("Enter a playlist URL:")],
    [sg.Input(key="url")],
    [sg.Text("Enter the download path:")],
    [sg.Input(key="path"), sg.FolderBrowse()],
    [sg.Button("Download"), sg.Cancel()],
    [sg.Text("Items downloaded:", size=(15, 1)), sg.Text(key="items", size=(5, 1))]
]

# Create the window
window = sg.Window("Playlist Downloader", layout)

# Event loop
while True:
    event, values = window.read()

    # If the user clicks the "Download" button
    if event == "Download":
        url = values["url"]
        path = values["path"]

        # Set the download options
        ydl_opts = {
            "outtmpl": os.path.join(path, "%(title)s.%(ext)s"),
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],

        }

        # Create a thread to download the playlist
        thread = threading.Thread(target=download, args=(ydl_opts, url))
        thread.start()

    # If the user clicks the "Cancel" button or closes the window
    if event in (sg.WIN_CLOSED, "Cancel"):
        break

# Clean up
window.close()


# Progress hook function

