# first pip install pytube
import tkinter as tk
from pytube import YouTube
import time


info = []

# function to get the link 
def get_info():
    link = entry1.get()
    resolution = entry2.get()
    info.append(link)
    info.append(resolution.lower())

#this function to call get_info function to get the link and resolution and download the video
def download():
    get_info()
    link = info[0]
    yt = YouTube(link)
    if info[1] == "highest":
        yd = yt.streams.get_highest_resolution()
    else:
        yd = yt.streams.get_lowest_resolution()
    yd.download(
        "/home/dci-student/Desktop/Python/Projects/YouTube_Downloader/YouTube_downloads") 
    time.sleep(5)
    root.event_generate("<<TaskFinished>>")

#this function to warn the user that the download was completed
def on_task_finished(event):
    done = tk.Tk()
    done.title("YouTube Downloader")
    done.geometry("300x100+700+400")
    label_d = tk.Label(done, text=f"Download completed with {info[1]} resolution")
    label_d.pack()
    ok = tk.Button(done, text="ok", command=done.destroy, background="gray25")
    ok.pack()

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
root.configure(background="red2")
root.geometry("600x200+700+300")


# Create a label and entry widget
label1 = tk.Label(root, text="Enter the Youtube link: ", width=80, background="red2")
label1.pack()


entry1 = tk.Entry(root, width=50, background="gray62")
entry1.pack()

label2 = tk.Label(
    root, text="Please enter the resolution for your download(highest or lowest): ", width=80, background="red2")
label2.pack()
entry2 = tk.Entry(root, width=50, background="gray62")
entry2.pack()


# Create a button to trigger input retrieval
dl = tk.Button(root, text="Download", command=download, background="gray25")
dl.pack()
exit = tk.Button(root, text="Exit", command=root.destroy, background="gray25")
exit.pack()

root.bind("<<TaskFinished>>", on_task_finished)
root.mainloop()








