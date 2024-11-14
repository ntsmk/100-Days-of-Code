from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        # todo set up UI here 6 grids - > look for reference
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        canvas = Canvas(width=300, height=250, bg="White")
        canvas.grid(column=0, row=1, columnspan=2)

        score = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        score.grid(column=1, row=0)

        text = Label(text="this is test", bg="white", font=("Arial", 20, "italic"))
        text.grid(column=0, row=1, columnspan=2)

        true_button_img = PhotoImage(file="images/true.png")
        true_button = Button(image=true_button_img, highlightthickness=0)
        true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        false_button = Button(image=false_button_img, highlightthickness=0)
        false_button.grid(column=1, row=2)


        self.window.mainloop()

