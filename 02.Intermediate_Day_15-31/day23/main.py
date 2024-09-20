import time
from turtle import Screen
from turtle_itself import TurtleItself
from car import Car
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.title("welcome to turtle crossing game!")
screen.tracer(0)

t = TurtleItself()
car = Car()
score = Score()

screen.listen()
screen.onkey(t.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.move()

# detect if the turtle crossed = level up = car speed up
    if t.ycor() > 280:
        car.speedup()
        t.go_home()
        score.levelup()

    for i in car.cars:
        if t.distance(i) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()