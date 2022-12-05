from pytube import *
from moviepy.editor import *
import os
from time import sleep

def download_video(input_text, convert_mp3):
    if input_text == "youtube playlist":
        downloaded_number = 1

        if convert_mp3 == "1":
            #Looping through the list of youtube videos (YouTube object)
            for video in yt_vid.videos:
                print(f"Downloading... [{downloaded_number}/{yt_vid.length}]")
                video_mp4 = video.streams.get_highest_resolution().download(download_directory) #Downloading the mp4 with the specified filename
                sleep(1)
                downloaded_number += 1
        #Check if user wants it in mp3
        elif convert_mp3 == "2":
             
            for video in yt_vid.videos:
                print(f"Downloading... [{downloaded_number}/{yt_vid.length}]")
                video_mp4 = video.streams.get_lowest_resolution().download(download_directory) #Downloading the mp4 with the specified filename
                sleep(1)

                convert_to_mp3(video_mp4)
                downloaded_number += 1
        
    elif input_text == "youtube video":
        print("Downloading...")
        video_mp4 = yt_vid.streams.get_highest_resolution().download(download_directory)
        sleep(1)
        #Checks if user wants it in mp3
        if convert_mp3 == "2":
                convert_to_mp3(video_mp4)
    else:
        print("invalid Choice")

def convert_to_mp3(video_mp4):
    root, ext = os.path.splitext(video_mp4) #Unpacking
    new_file = root + ".mp3"
    os.rename(video_mp4, new_file)

def choose_input(input_text):
    if input_text == "youtube playlist":
        url = input("Enter youtube URL: ") #Ask for youtube playlist url
        return Playlist(url) #Playlist object
    elif input_text == "youtube video":
        url = input("Enter youtube URL: ") #Ask for youtube playlist url
        return YouTube(url)
    else:
        print("Invalid Choice")

# This is a python standard, basically separates the code you are running from user defined fucntions
if __name__ == '__main__':
    download_directory = "E:\Andrew\Songs Audio\J-Pop"

    input_type = input("YouTube Playlist, or YouTube Video: ")
    input_type = input_type.lower()
    yt_vid = choose_input(input_type)

    should_convert_mp3 = input("""
    Choose one number:

    [1] Download in mp4
    [2] Convert to mp3
    """)
    download_video(input_type, should_convert_mp3)

    print("Download Complete!")
    