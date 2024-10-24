from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
# todo Step 1 - Create the User Interface (UI) with Tkinter
# only 2 X 2 grid. use card_front.png

window = Tk()
window.title("Flash card app")

# canvas
canvas = Canvas(width=800, height=526)
window.config(padx=50, pady=50)
canvas.grid(column=0, row=0)

# button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=0)
left = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left, highlightthickness=0)
wrong_button.grid(column=0, row=0)

window.mainloop()
