from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update()

    def update(self):
        self.goto(-300,250)
        self.write(f"Level: {self.score}", False, ALIGN, FONT)

    def levelup(self):
        self.score += 1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGN, FONT)
