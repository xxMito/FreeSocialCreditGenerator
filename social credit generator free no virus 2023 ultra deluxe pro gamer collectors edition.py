import os
import threading
import random
from tkinter import *
import playsound
from PIL import ImageTk, Image

working_dir = os.getcwd()

# SONGS
songs_dir = 'songs'
full_songs_dir = os.path.join(working_dir, songs_dir)

songs = os.listdir(songs_dir)
songs_iterator = os.scandir(songs_dir)
songs_dirEntries = [x for x in songs_iterator]
r = random.choice(songs)
full_song_path = os.path.join(full_songs_dir, r)

# SFX
sfx_dir = 'sfx'
full_sfx_dir = os.path.join(working_dir, sfx_dir)

sfx = os.listdir(sfx_dir)
sfx_iterator = os.scandir(sfx_dir)
sfx_dirEntries = [x for x in sfx_dir]



# Create an instance of Tkinter Frame
win = Tk()
win.title('Free Social Credit Generator No Virus 2023 Ultra Deluxe Pro Gamer Collectors Edition')


# Set the geometry of Tkinter Frame
win.geometry("700x450")

# Open the Image File
bg = ImageTk.PhotoImage(file="flagcn.png")

# Create a Canvas
canvas = Canvas(win, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.create_text(450, 20, text="免费的社会信用生成器", font=("Arial", 25))



total_social_credits = IntVar()
entered_amount = StringVar()
sfx_counter = 0


def add_credit():
   global sfx_counter
   try:
      amount_to_add = int(entered_amount.get())
   except:
      return None
   previous_total = total_social_credits.get()
   total_social_credits.set(previous_total + amount_to_add)

   # play a victory sound
   if sfx_counter == 1:
      sfx_counter = 0
   else:
      sfx_counter = 1

   r_sfx = sfx[sfx_counter]
   full_sfx_path = os.path.join(full_sfx_dir, r_sfx)
   playsound.playsound(full_sfx_path, block=False)


button_entry = Button(win, text="Enter amount", command=add_credit)
button_entry.place(x=300, y=200)
amount_entry = Entry(win, textvariable=entered_amount)
amount_entry.place(x=400, y=200)

btnAddCredit = Button(win, command=add_credit, text="Generate Credits")
# Function to resize the window


def resize_image(e):
   global image, resized, image2
   image = Image.open("flagcn.png")
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=bg, anchor='nw')
   canvas.create_text(450, 20, text="免费的社会信用生成器", font=("Arial", 25))
   # canvas.create_text(100, 300, text=str(total_social_credits.get()), font=("Arial", 25))


label_total = Label(win, textvariable=total_social_credits, font=("Arial", 25))
label_total.place(x=100, y=300)
# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)


def loopSound():
   while True:
      playsound.playsound(full_song_path, block=True)


loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True
loopThread.start()

win.mainloop()
