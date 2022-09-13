import os
import threading
import random
from tkinter import *
import playsound
from PIL import ImageTk, Image

working_dir= os.getcwd()
songs_dir = 'songs'
full_songs_dir = os.path.join(working_dir, songs_dir)

songs = os.listdir(songs_dir)
songs_iterator = os.scandir(songs_dir)
songs_dirEntries = [x for x in songs_iterator]

# Create an instance of Tkinter Frame
win = Tk()
win.title('social credit generator free no virus 2023 ultra deluxe pro gamer collectors edition')
r = random.choice(songs)
full_song_path = os.path.join(full_songs_dir, r)


# Set the geometry of Tkinter Frame
win.geometry("700x450")

# Open the Image File
bg = ImageTk.PhotoImage(file="flagcn.png")

# Create a Canvas
canvas = Canvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.create_text(450, 20, text="free social credit generator 2023", font=("Arial", 25))


# Function to resize the window
def resize_image(e):
   global image, resized, image2
   image = Image.open("flagcn.png")
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=bg, anchor='nw')
   canvas.create_text(450, 20, text="free social credit generator 2023", font=("Arial", 25))


# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)

def loopSound():
   while True:
      playsound.playsound(full_song_path, block=True)


loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True
loopThread.start()

win.mainloop()
