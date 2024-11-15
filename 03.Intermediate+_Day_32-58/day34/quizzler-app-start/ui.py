from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        # todo set up the actual text and set up padding as well?
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.canvas.create_text(150, 125,
                           text="Dream is the most important. Even more important than actual life. Dream won’t die.",
                           font=("Arial", 20, "italic"), width=260)

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()

