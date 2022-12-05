import tkinter as tk
from downloadyoutube import *



def clicked_mp3():
    mp3_btn.config(relief="sunken")
    mp4_btn.config(relief="raised")
    state = 2
    

def clicked_mp4():
    mp4_btn.config(relief="sunken")
    mp3_btn.config(relief="raised")
    state = 1



#Create window
window = tk.Tk()
window.geometry("650x750")
window.title("YouTube Converter")
window.resizable(width=False, height=False)

frame = tk.Frame(window)
frame.pack()

link_entry = tk.Entry(frame, width = 40, font= 16)
link_entry.grid(row= 3, column=1,sticky="e", padx=5, pady= 5)

label = tk.Label(frame, text= "Enter YouTube Link:",font= 16)
label.grid(row=3, column=0, padx= 1, pady= 5, sticky= "w")

# Converting label changes based on button clicked

label2 = tk.Label(frame, text= "Convert to: ", font= 16)
label2.grid(row=5, column=0, pady=10 ,sticky="e")

mp3_btn = tk.Button(frame, text= "Convert to Mp3", font = 16, command= clicked_mp3)
mp3_btn.grid(row=5, column=1, padx= 5, pady=10, sticky="e" )

mp4_btn = tk.Button(frame, text= "Convert to Mp4", font = 16, command= clicked_mp4)
mp4_btn.grid(row=5, column=1, padx= 5, pady= 10, sticky= "w")

label3 = tk.Label(frame, text="Choose Directory: ", font = 16)
label3.grid(row=4, column= 0, padx= 5, pady= 10, sticky= "e")


window.mainloop()


