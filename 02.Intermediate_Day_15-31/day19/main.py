from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def forwards():
    t.forward(10)

def backwards():
    t.backward(10)

def clockwise():
    t.right(10)

def counter_clockwise():
    t.left(10)

def clear():
    t.clear()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")


screen.listen()

screen.exitonclick()
