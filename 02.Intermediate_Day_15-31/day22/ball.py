from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_position = 10
        self.y_position = 10


    def move(self):
        new_x = self.xcor() + self.x_position
        new_y = self.ycor() + self.y_position
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_position *= -1

    def bounce_x(self):
        self.x_position *= -1

    def reset_ball(self):
        self.home()
        self.bounce_x()
