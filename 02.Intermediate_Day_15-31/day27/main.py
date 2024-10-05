#from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("welcome to my program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100,y=0)
my_label.grid(column=0, row=0)

def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="push!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

input = tkinter.Entry(width=10)
# input.pack()
# print(input.get())
input.grid(column=2, row=2)



window.mainloop()