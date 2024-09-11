from turtle import Turtle, Screen
import random as random

# fetching color from img file.
# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('img.jpg', 30)
#
# def getting_color(color):
#     color_list = []
#     for color_from_list in color:
#         r = color_from_list.rgb.r
#         g = color_from_list.rgb.g
#         b = color_from_list.rgb.b
#         color_list.append((r, g, b))
#     return color_list
#
# a = getting_color(colors)
# print(a)

color_list = [(203, 165, 108), (152, 74, 48), (234, 238, 243), (52, 93, 124), (170, 153, 41), (223, 202, 136), (137, 32, 21), (132, 163, 185), (47, 121, 88), (198, 91, 72), (15, 99, 73), (70, 47, 39), (147, 179, 148), (98, 73, 75), (162, 142, 157), (234, 175, 164), (55, 46, 49), (184, 205, 172), (24, 81, 87), (38, 61, 74), (142, 22, 25), (85, 146, 126), (45, 65, 85), (175, 91, 94), (214, 177, 183), (18, 70, 64), (109, 125, 151)]

t = Turtle()
screen = Screen()
# need this to choose randomly from color list
screen.colormode(255)

# def select_color():
#     return t.color(random.choice(color_list))

# set arrow in the default position
t.penup()
default_x = -250
default_y = -250
t.goto(default_x,default_y)

# set 0 for the counter
x = 0
y = 0

# drawing dots
while y < 10:
    while x < 10:
        # select_color()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
        x += 1
    x = 0
    y += 1
    t.goto(default_x, (default_y+(y*50)))
t.ht()


screen.exitonclick()