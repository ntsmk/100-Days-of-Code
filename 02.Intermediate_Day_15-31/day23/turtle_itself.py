from turtle import Turtle

START_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class TurtleItself(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def gohome(self):
        self.goto(START_POSITION)
