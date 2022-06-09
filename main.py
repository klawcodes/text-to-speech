from cgitb import text
from logging import root
import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop

root=Tk()

textv=StringVar()

obj=LabelFrame(root,text="Text to Speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=20,bg="black", fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)


root.title("Text to Speech by KLAW")
root.geometry("400x500")
root.resizable(False,False)
root.mainloop()