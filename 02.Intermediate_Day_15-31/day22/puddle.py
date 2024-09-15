from turtle import Turtle

UP = 90
DOWN = 270

class Puddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.goto(position)
        self.setheading(UP)

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)
