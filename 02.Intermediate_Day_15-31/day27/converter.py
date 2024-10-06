import tkinter

# window config
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)


# labels
# miles
my_label = tkinter.Label(text="Miles", font=("Helvetica", 13))
my_label.grid(column=2, row=0)

# is equal to
my_label = tkinter.Label(text="is equal to", font=("Helvetica", 13))
my_label.grid(column=0, row=1)

# 0
my_label2 = tkinter.Label(text=0, font=("Helvetica", 13))
my_label2.grid(column=1, row=1)

# km
my_label = tkinter.Label(text="Km", font=("Helvetica", 13))
my_label.grid(column=2, row=1)

# button
def button_clicked():
    my_label2["text"] = int(float(input.get())*1.60934)

button = tkinter.Button(text="Calcurate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()