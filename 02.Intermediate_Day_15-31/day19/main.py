from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def forwards():
    t.forward(10)

def backwards():
    t.backward(10)

def clear():
    t.clear()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(clear, "c")


screen.listen()

screen.exitonclick()
