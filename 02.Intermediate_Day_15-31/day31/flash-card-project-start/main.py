from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/french_words.csv")
dict = df.to_dict(orient="records")
# current_word = random.choice(dict)
current_word = {}

# ---------------------------- NEW FLASH CARDS ------------------------------- #
def generate():
    global current_word
    current_word = random.choice(dict)
    canvas.itemconfig(word, text=current_word["French"])
    canvas.itemconfig(language,text="French")

def flip():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(word, text=current_word["English"], fill="White")
    canvas.itemconfig(language,text="English", fill="White")


# todo need to put new french word again
def cancel():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(language, text="", fill="Black")
    canvas.itemconfig(word, text="", fill="Black")
    generate()
    window.after(3000, flip)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front)
canvas.grid(column=0, row=0, columnspan=2)

# label
language = canvas.create_text(370, 120, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(370, 230, text="", font=("Arial", 60, "bold"))

# button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=cancel)
right_button.grid(column=1, row=1)

left = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left, highlightthickness=0, command=generate)
wrong_button.grid(column=0, row=1)

generate()

window.mainloop()
