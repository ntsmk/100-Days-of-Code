from turtle import Turtle

ALIGN = "center"
FONT = ('Courier New', 40, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_r = 0
        self.score_l = 0
        self.update_r()
        self.update_l()

    def update_r(self):
        self.goto(200,230)
        self.write(self.score_r, False, ALIGN, FONT)

    def update_l(self):
        self.goto(-200, 230)
        self.write(self.score_l, False, ALIGN, FONT)

    def add_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_r()

    def add_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_l()

