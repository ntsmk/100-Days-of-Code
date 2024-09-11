from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# def forwards():
#     t.forward(10)
# def backwards():
#     t.backward(10)
# def clockwise():
#     t.right(10)
# def counter_clockwise():
#     t.left(10)
# def clear():
#     t.clear()
#
# screen.onkey(forwards, "w")
# screen.onkey(backwards, "s")
# screen.onkey(counter_clockwise, "a")
# screen.onkey(clockwise, "d")
# screen.onkey(clear, "c")
# screen.listen()
# thislist = ["t1", "t2", "t3", "t4", "t5", "t6"] # you don't have to create by distingush number
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-100+40*i)

#
# t1 = Turtle(shape="turtle")
# t1.color(colors[0])
# t1.penup()
# t1.goto(x=-230,y=-100) 1 * -100
#
# t2 = Turtle(shape="turtle")
# t2.color(colors[1])
# t2.penup()
# t2.goto(x=-230,y=-60) 2 * -30
#
# t3 = Turtle(shape="turtle")
# t3.color(colors[2])
# t3.penup()
# t3.goto(x=-230,y=-20) 3 * -7
#
# t4 = Turtle(shape="turtle")
# t4.color(colors[3])
# t4.penup()
# t4.goto(x=-230,y=20) 4 * 5
#
# t5 = Turtle(shape="turtle")
# t5.color(colors[4])
# t5.penup()
# t5.goto(x=-230,y=60) 5 * 10
#
# t6 = Turtle(shape="turtle")
# t6.color(colors[5])
# t6.penup()
# t6.goto(x=-230,y=100) 6 * 17
#



screen.exitonclick()
