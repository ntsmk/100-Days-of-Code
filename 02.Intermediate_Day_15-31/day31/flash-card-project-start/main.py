from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- NEW FLASH CARDS ------------------------------- #
df = pandas.read_csv("data/french_words.csv")
dict = df.to_dict(orient="records")

def generate():
    thisdict = random.choice(dict)
    word.config(text=thisdict["French"])
    language.config(text=list(thisdict.keys())[0])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash card app")

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=front)
canvas.grid(column=0, row=0, columnspan=2)

# label
language = Label(text="", font=("Arial", 40, "italic"), bg="white")
language.place(x=300, y=110)

word = Label(text="", font=("Arial", 60, "bold"),  bg="white")
word.place(x=270, y=213)

# button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=generate)
right_button.grid(column=1, row=1)

left = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left, highlightthickness=0, command=generate)
wrong_button.grid(column=0, row=1)

generate()
# todo Step 3 - Flip the Cards
# IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.
back = PhotoImage(file="images/card_back.png")


window.mainloop()
