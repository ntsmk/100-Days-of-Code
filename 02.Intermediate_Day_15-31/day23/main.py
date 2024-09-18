import time
from turtle import Screen
from turtle_itself import TurtleItself
from car import Car

screen = Screen()
screen.setup(width=800, height=600)
screen.title("welcome to turtle crossing game!")
screen.tracer(0)

t = TurtleItself()
car = Car()

screen.listen()
screen.onkey(t.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.move()


# todo  detect if the turtle crossed = level up = car speed up
# need level class

# todo detect if the turtle hit the car = game over
# in level class, put game over as well


screen.exitonclick()