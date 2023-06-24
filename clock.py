from tkinter import *
from tkinter.ttk import *

from time import strftime

#ui for clock
root = Tk()
root.title("Clock")
#time
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)


label = Label(root, font=("ds-digital",80),background = "black",foreground = "pink")
label.pack(anchor = "center")

time()
mainloop()

