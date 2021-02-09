from tkinter import *

root = Tk()

root.title("RPi Arcade")
root.config(bg = "#373737")
root.attributes('-fullscreen', True)

Title = Label(root, text = "Game Selection", fg = "#C7C7C7", bg = "#373737", font = ("SF Pro Display Ultralight", 120))
Title.place(anchor = N, relx = 0.5)

root.mainloop()