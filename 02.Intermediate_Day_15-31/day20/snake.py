from turtle import Screen, Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


t_list = ["t1", "t2", "t3"]

class Snake():
    def __init__(self):
        self.create_snake()
        self.head = t_list[0]

    def create_snake(self):
        for t_index in range(3):
            t_list[t_index] = Turtle(shape="square")
            t_list[t_index].color("white")
            t_list[t_index].penup()
            t_list[t_index].goto(-20*1*t_index, 0)

    def move(self):
        for i in range(len(t_list) - 1, 0, -1):
            new_x = t_list[i - 1].xcor()
            new_y = t_list[i - 1].ycor()
            t_list[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)