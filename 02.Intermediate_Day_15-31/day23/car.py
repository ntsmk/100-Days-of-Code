from turtle import Turtle
import random

COLOR = ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []

class Car():
    def __init__(self):
        self.generate()


    def generate(self):
        for car in range(50):
            car = Turtle(shape="turtle")
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(random.randint(-300, 300), random.randint(-260, 260))
            car.setheading(180)
            car.color(random.choice(COLOR))
            cars.append(car)

    def move(self):
        for car in cars:
            car.forward(STARTING_MOVE_DISTANCE)

