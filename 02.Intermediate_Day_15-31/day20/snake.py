from turtle import Screen, Turtle
import time

t_list = ["t1", "t2", "t3"]

class Snake():
    def __init__(self):
        self.create_snake()

    def create_snake(self):
        for t_index in range(3):
            t_list[t_index] = Turtle(shape="square")
            t_list[t_index].color("white")
            t_list[t_index].penup()
            t_list[t_index].goto(-20*1*t_index, 0)

    def move(self):
        for i in range(len(t_list) - 1, 0, -1):
            new_x = t_list[i -1].xcor()
            new_y = t_list[i - 1].ycor()
            t_list[i].goto(new_x,new_y)
        t_list[0].forward(20)

    def up(self):
        t_list[0].setheading(90)


    def down(self):
        t_list[0].setheading(270)

    def left(self):
        t_list[0].setheading(180)


    def right(self):
        t_list[0].setheading(0)