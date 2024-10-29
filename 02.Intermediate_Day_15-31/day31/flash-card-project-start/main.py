from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
df = pandas.read_csv("data/french_words.csv")
dict = df.to_dict(orient="records")
current_word = {}

# ---------------------------- FLASH CARDS ------------------------------- #
def generate():
    global current_word

    current_word = random.choice(dict)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(word, text=current_word["French"], fill="Black")
    canvas.itemconfig(language,text="French", fill="Black")
    window.after_cancel(timer)
    window.after(3000, flip)

def flip():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(word, text=current_word["English"], fill="White")
    canvas.itemconfig(language,text="English", fill="White")


# todo Step 4 - Save Your Progress
# already saving the CSV file, converting to CSV. Using all hints provided. Need to figure out what is rest of tasks
def check():
    dict.remove(current_word)
    new_df = pandas.DataFrame.from_dict(dict)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    generate()


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
right_button = Button(image=right, highlightthickness=0, command=check)
right_button.grid(column=1, row=1)

left = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left, highlightthickness=0, command=generate)
wrong_button.grid(column=0, row=1)

generate()

window.mainloop()
