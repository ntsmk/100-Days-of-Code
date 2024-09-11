from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("welcome to my snake game")
t_list = ["t1", "t2", "t3"]

for t_index in range(3):
    t_list[t_index] = Turtle(shape="square")
    t_list[t_index].color("white")
    t_list[t_index].penup()
    t_list[t_index].goto(-20*1*t_index, 0)

game_is_on = True
while game_is_on:
    for t_index in t_list:
        t_index.forward(20)

screen.exitonclick()