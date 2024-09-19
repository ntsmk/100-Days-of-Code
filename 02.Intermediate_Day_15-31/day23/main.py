import time
from turtle import Screen
from turtle_itself import TurtleItself
from car import Car
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.title("welcome to turtle crossing game!")
screen.tracer(0)

t = TurtleItself()
car = Car()
score = Score()

screen.listen()
screen.onkey(t.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.move()

# detect if the turtle crossed = level up = car speed up
    if t.ycor() > 280:
        car.speedup()
        t.gohome()
        score.levelup()

# todo detect if the turtle hit the car = game over
# in level class, put game over as well
#     if t.distance(car.cars_list):
#         game_is_on = False
#         score.gameover


screen.exitonclick()