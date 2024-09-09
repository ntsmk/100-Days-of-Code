from turtle import Turtle, Screen
from random import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('#f9d910')

def change_color():
    R = random()
    B = random()
    G = random()

    timmy_the_turtle.color(R, G, B)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# from random import random

for i in range(100):
    steps = int(random() * 100)
    # angle = int(random() * 360)
    change_color()
    timmy_the_turtle.right(90)
    timmy_the_turtle.fd(steps)
    timmy_the_turtle.speed(8)

# for _ in range(10):
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)



# for i in range(3,9):
#     for _ in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)
#     change_color()

screen = Screen()
screen.exitonclick()
