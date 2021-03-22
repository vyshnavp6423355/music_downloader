from PIL import Image, ImageTk, ImageDraw
from tkinter import *

root = Tk()

bg = PhotoImage(file = "assets/UI.png")
root.iconbitmap("assets/logo.ico")
mdl = PhotoImage(file="assets/mdl.png")
ytdl = PhotoImage(file="assets/ytdl.png")
spo = PhotoImage(file="assets/spo.png")
sd = PhotoImage(file="assets/sd.png")
ytd = PhotoImage(file="assets/ytd.png")
spod = PhotoImage(file="assets/spod.png")
cvk = PhotoImage(file="assets/cvk.png")

def single_download_ui(ob1):
    bg = PhotoImage(file = "assets/UI.png")
    ob1.withdraw()
    ob = Toplevel()
    ob.geometry('960x588')
    canvas = Canvas(ob, bg = 'white', height= 588, width= 960)
    canvas.pack(expand= YES, fill= BOTH)
    canvas.create_image(0,0,image = bg, anchor=NW)
    canvas.create_text(700,500, text="Hello World!",fill="white",font="Times 20 bold")
    ob.mainloop()

root.title("Music Downloader")
root.geometry('960x588')

canvas = Canvas(root, bg = 'white', height= 588, width= 960)
canvas.pack(expand= YES, fill= BOTH)
canvas.create_image(0,0,image = bg, anchor=NW)
mdlb = Button(root, image=mdl, compound=LEFT, borderwidth=0, border=0, command=(lambda: single_download_ui(root)))
mdlb.place(x=176,y=224)
canvas.create_image(235,375, image=sd)
# canvas.create_text(700,500, text="Hello World!",fill="white",font="Times 20 bold")

ytdlb = Button(root, image=ytdl, compound=LEFT, borderwidth=0, border=0, command={}) 
ytdlb.place(x=410,y=224)
canvas.create_image(475,375, image=ytd)

spob = Button(root, image=spo, compound=LEFT, borderwidth=0, border=0, command={}) 
spob.place(x=640,y=224)
canvas.create_image(705,375, image=spod)
canvas.create_image(890,550, image=cvk)

frame = Frame(root)

canvas.pack()
root.mainloop()

