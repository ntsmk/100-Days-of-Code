from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('#f9d910')

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# import turtle as t
# from random import random
#
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
#     t.speed(8)

screen = Screen()
screen.exitonclick()
