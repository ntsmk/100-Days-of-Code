from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score} ", False, align="center", font=('Courier New', 20, 'normal'))

    def add(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", False, align="center", font=('Courier New', 20, 'normal'))

