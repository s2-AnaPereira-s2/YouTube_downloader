#first pip install pytube

from pytube import YouTube
from sys import argv

#here the link you will put in the terminal when run the program
link = argv[1]
yt = YouTube(link)

#here you can choose the resolution that suits you better, in my case I got the lowest, but you can also use get_highest_resolution()
yd = yt.streams.get_lowest_resolution()

#here inside the ("") you have to put the path for the folder that you want to store the videos
yd.download("path")

