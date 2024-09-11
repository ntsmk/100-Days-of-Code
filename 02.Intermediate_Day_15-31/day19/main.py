from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move():
    t.forward(100)

screen.onkey(move, "space")
screen.listen()

screen.exitonclick()
