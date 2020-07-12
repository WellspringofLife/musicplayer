import pygame
import tkinter

player = tkinter.Tk()

player.title("Player")
player.geometry("205x340")

file = "song.mp3"

def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

PlayButton = tkinter.Button(player, width=5, height=3, text="play", command=play)
PlayButton.pack(fill="x")

StopButton = tkinter.Button(player, width=5, height=3, text="stop", command=stop)
StopButton.pack(fill="x")

label1 = tkinter.LabelFrame(player, text="Song Name")
label1.pack(fill="both", expand="yes")
contents1 = tkinter.Label(label1, text=file)
contents1.pack()

player.mainloop()

