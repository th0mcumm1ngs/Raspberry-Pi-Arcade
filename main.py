from tkinter import *
from Games.Space_Invaders.Space_Invaders import *

root = Tk()

root.title("RPi Arcade")
root.config(bg = "#373737")
root.attributes('-fullscreen', True)

Title = Label(root, text = "Game Selection", fg = "#C7C7C7", bg = "#373737", font = ("SF Pro Display Ultralight", 120))
Title.place(anchor = N, relx = 0.5)


# Load all the thumbnails.
space_invaders_thumb = PhotoImage(file = "Games/Space_Invaders/Space Invaders Thumbnail.png")

# Game Thumbnail Spaces

## Top Left
tl_game_button = Button(root, image = space_invaders_thumb, command = space_invaders_main_run)
tl_game_button.place(anchor = N, x = 361, y = 254)

## Top Middle
tm_game_button = Button(root)
tm_game_button.place(anchor = N, x = 960, y = 254)

## Top Right
tr_game_button = Button(root)
tr_game_button.place(anchor = N, x = 1559, y = 254)

## Bottom Left
bl_game_button = Button(root)
bl_game_button.place(anchor = N, x = 361, y = 675)

## Bottom Midddle
bm_game_button = Button(root)
bm_game_button.place(anchor = N, x = 960, y = 675)

## Bottom Right
br_game_button = Button(root)
br_game_button.place(anchor = N, x = 1559, y = 675)

root.mainloop()