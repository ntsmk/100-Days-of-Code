from turtle import Turtle, Screen

tom = Turtle()
my_screen = Screen()
tom.shape("turtle")
tom.color("green")
tom.forward(100)
tom.back(300)
tom.clear()

print(my_screen.canvheight)
my_screen.exitonclick()