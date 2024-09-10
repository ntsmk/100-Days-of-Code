from turtle import Turtle, Screen
import random as random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('#f9d910')

direction = [0,90,180,270]

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    return timmy_the_turtle.color(R, G, B)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# from random import random

# timmy_the_turtle.pensize(5)

# for i in range(250):
#     # steps = int(random() * 100)
#     # angle = int(random() * 360)
#     change_color()
#     timmy_the_turtle.right(random.choice(direction))
#     timmy_the_turtle.fd(20)
#     timmy_the_turtle.speed("fastest")

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

for i in range(0,361, 10):
    timmy_the_turtle.speed("fastest")
    change_color()
    r = 100
    timmy_the_turtle.circle(r)
    timmy_the_turtle.setheading(i)

screen = Screen()
screen.exitonclick()
