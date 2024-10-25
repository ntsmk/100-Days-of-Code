from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/french_words.csv")
dict = df.to_dict(orient="records")

# ---------------------------- NEW FLASH CARDS ------------------------------- #
def generate():
    thisdict = random.choice(dict)
    canvas.itemconfig(word, text=thisdict["French"])
    canvas.itemconfig(language,text=list(thisdict.keys())[0])

def flip():
    # todo pick the English translation, not random word
    # todo figure out how to count 3 seconds
    # timer = window.after(1000, count_down, count-1) how to modify this
    thisdict = random.choice(dict)
    canvas.itemconfig(word, text=thisdict["English"], fill="White")
    canvas.itemconfig(language,text=list(thisdict.keys())[1], fill="White")
    canvas.itemconfig(canvas_image, image=back)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash card app")

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=front)
canvas.grid(column=0, row=0, columnspan=2)

# label
language = canvas.create_text(370, 120, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(370, 230, text="", font=("Arial", 60, "bold"))

# button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=flip)
right_button.grid(column=1, row=1)

left = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left, highlightthickness=0, command=generate)
wrong_button.grid(column=0, row=1)

generate()
# flip()

window.mainloop()
