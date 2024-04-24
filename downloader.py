from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

yd = yt.streams.get_lowest_resolution()
yd.download("/home/dci-student/Desktop/Python/Projects/YouTube_Downloader/YouTube_downloads")