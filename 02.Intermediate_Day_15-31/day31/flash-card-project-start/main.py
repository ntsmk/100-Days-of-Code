from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- NEW FLASH CARDS ------------------------------- #
# todo Step 2 - Create New Flash Cards
# 1. Read the data from the french_words.csv file in the data folder.
# use DataFrame.to_dict(orient="records")
df = pandas.read_csv("data/french_words.csv")
dict = df.to_dict(orient="records")
print(dict)

# 2. Pick a random French word/translation and put the word into the flashcard when the button was hit
# use random function to pick up the word from dict


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash card app")

# todo need to put label French and word
# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=front)
canvas.grid(column=0, row=0, columnspan=2)

# button
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0)
right_button.grid(column=1, row=1)

left = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=left, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# label
language_french = Label(text="Title", font=("Arial", 40, "italic"), bg="white")
language_french.place(x=300, y=110)

word = Label(text="word", font=("Arial", 60, "bold"),  bg="white")
word.place(x=270, y=213)

window.mainloop()
