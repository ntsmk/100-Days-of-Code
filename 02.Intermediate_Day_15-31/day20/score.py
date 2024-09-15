from turtle import Turtle

ALIGN = "center"
FONT = ('Courier New', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update()

    def update(self):
        self.write(f"Score: {self.score} ", False, ALIGN, FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER...", False, ALIGN, FONT)

    def add(self):
        self.score += 1
        self.clear()
        self.update()

