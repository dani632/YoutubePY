from sys import argv
from pytube import YouTube

import os.path

#check if any path was given in an argument
if len(argv) > 1:
    path = argv[1]
#if non was given add a folder path
else:
    path = "/Users/ADMIN/Documents"

#Add the an input field for YouTube video link

inp = input()

yt = YouTube(inp)

def _inp(title, views):
    title = yt.title
    views = yt.views
    print("Title : " ,title , "Views : " ,views)

#Get the video resoluction
yr = yt.streams.get_highest_resolution()

#Call the download API
yr.download(path)

