from tkinter import *
import pyttsx3

root = Tk()
root.title("Text To Speech")
root.geometry("600x500")
root.iconbitmap('C:/Users/HP/Desktop')

def talk():
    e = pyttsx3.init()
    e.say(my_entry.get())
    e.runAndWait()
    my_entry.delete(0,END)

my_entry = Entry(root,font=("Helvetica",28))
my_entry.pack(pady=20)

my_button=Button(root,text="Speak",bg="#bfde23",padx=20,pady=9,command=talk)
my_button.pack(padx=20)

root.mainloop()