from turtle import Screen
from puddle import Puddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("welcome to my PONG game!")
screen.tracer(0)

puddle = Puddle()

screen.listen()
screen.onkey(puddle.up, "Up")
screen.onkey(puddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.001)


screen.exitonclick()
