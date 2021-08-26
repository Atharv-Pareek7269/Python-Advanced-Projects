#importing essentials 
from tkinter import *
from tkinter.ttk import*
from time import strftime
import datetime

#initialising Tkinter 
root = Tk()
root.title("My clock") #Giving title

def time():
    string = strTime = datetime.datetime.now().strftime("%H:%M:%S") 
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=("DS-DIGITAl", 150), background="black", foreground="cyan")
label.pack(anchor='center')
time()


mainloop()
