from turtle import Turtle
import random

COLOR = ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []

class Car(Turtle):
    def __init__(self):
        for i in range(5):
            super().__init__()
            self.shape("square")
            self.penup()
            self.shapesize(stretch_len=2, stretch_wid=1)
            self.goto(300, random.randint(-260, 260))
            self.setheading(180)
            self.color(random.choice(COLOR))

    def generate_car(self):
        pass
        
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

