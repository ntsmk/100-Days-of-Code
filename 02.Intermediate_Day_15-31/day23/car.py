from turtle import Turtle
from turtle_itself import TurtleItself
import random

COLOR = ["red", "blue", "yellow", "orange", "green", "purple", "pink", "grey"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars_list = []

class Car():
    def __init__(self):
        self.generate()

    def generate(self):
        for car in range(50):
            car = Turtle(shape="turtle")
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(random.randint(-400, 400), random.randint(-260, 260))
            car.setheading(180)
            car.color(random.choice(COLOR))
            cars_list.append(car)
            self.cars = cars_list

    def move(self):
        for car in cars_list:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -400:
                car.goto(random.randint(300, 400), random.randint(-260, 260))

    def speedup(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
