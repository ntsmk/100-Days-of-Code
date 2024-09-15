from turtle import Screen, Turtle

t_list = ["t1", "t2", "t3", "t4", "t5"]
UP = 90
DOWN = 270

class Puddle():
    def __init__(self):
        self.create_puddle()
        self.head = t_list[0]


    def create_puddle(self):
        for t_index in range(len(t_list)):
            t_list[t_index] = Turtle(shape="square")
            t_list[t_index].color("white")
            t_list[t_index].penup()
            t_list[t_index].goto(350, -20 * t_index)


    def moving_all(self):
        for i in range(len(t_list) - 1, 0, -1):
            new_x = t_list[i - 1].xcor()
            new_y = t_list[i - 1].ycor()
            t_list[i].goto(new_x, new_y)

    def up(self):
        self.head.setheading(UP)
        self.moving_all()
        self.head.forward(20)


    def down(self):
        self.head.setheading(DOWN)
        self.moving_all()
        self.head.forward(20)

