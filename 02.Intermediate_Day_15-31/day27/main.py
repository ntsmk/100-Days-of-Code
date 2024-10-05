#from tkinter import *
import tkinter

# window config
window = tkinter.Tk()
window.title("welcome to my program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100,y=0)
my_label.grid(column=0, row=0)

# button
def button_clicked():
    my_label["text"] = input.get()

button1 = tkinter.Button(text="push!", command=button_clicked)
# button.pack()
button1.grid(column=1, row=1)

button2 = tkinter.Button(text="push!", command=button_clicked)
button2.grid(column=2, row=0)

# entry
input = tkinter.Entry(width=10)
# input.pack()
# print(input.get())
input.grid(column=3, row=2)



window.mainloop()