#from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("welcome to my program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="push!", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()
# print(input.get())



window.mainloop()