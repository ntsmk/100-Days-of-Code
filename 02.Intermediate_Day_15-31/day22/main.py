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

    # detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect the collision with r_puddle
    if ball.distance(r_puddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detect the collision with l_puddle
    if ball.distance(l_puddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.reset_ball()



screen.exitonclick()
