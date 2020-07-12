import pygame
import tkinter
import os

player = tkinter.Tk()

player.title("Player")
player.geometry("205x340")

os.chdir("C:\\Users\\vivia\\PycharmProjects\\musicplayer\\venv\\music")
songlist = os.listdir()

playlist = tkinter.Listbox(player, highlightcolor="red", selectmode=tkinter.SINGLE)
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos + 1


pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkinter.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

var = tkinter.StringVar()
songtitle = tkinter.Label(player, textvariable=var)

PlayButton = tkinter.Button(player, width=5, height=3, text="play", command=play)
StopButton = tkinter.Button(player, width=5, height=3, text="stop", command=stop)

#label1 = tkinter.LabelFrame(player, text="Song Name")
#label1.pack(fill="both", expand="yes")
#contents1 = tkinter.Label(label1, text=file)


PlayButton.pack(fill="x")
StopButton.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand="yes")


player.mainloop()

