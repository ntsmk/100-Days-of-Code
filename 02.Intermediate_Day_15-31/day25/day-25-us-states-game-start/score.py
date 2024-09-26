from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, align=ALIGNMENT, font=FONT)
