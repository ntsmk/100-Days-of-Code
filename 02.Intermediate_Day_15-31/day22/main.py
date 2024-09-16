from turtle import Screen
from puddle import Puddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("welcome to my PONG game!")
screen.tracer(0)

r_puddle = Puddle((350,0))
l_puddle = Puddle((-350,0))
ball = Ball()


screen.listen()
screen.onkey(r_puddle.up, "Up")
screen.onkey(r_puddle.down, "Down")
screen.onkey(l_puddle.up, "w")
screen.onkey(l_puddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
