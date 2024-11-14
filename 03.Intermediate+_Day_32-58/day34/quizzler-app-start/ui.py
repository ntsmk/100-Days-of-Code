from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        # todo set up UI here 6 grids - > look for reference
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        canvas = Canvas(width=300, height=250, bg="White")
        canvas.grid(column=0, row=0)


        self.window.mainloop()

