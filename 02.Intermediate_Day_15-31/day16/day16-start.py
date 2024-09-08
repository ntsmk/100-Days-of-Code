# from turtle import Turtle, Screen
#
# tom = Turtle()
# my_screen = Screen()
# tom.shape("turtle")
# tom.color("green")
# tom.forward(100)
# tom.back(300)
# tom.clear()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon Name",["Pikachu", "Pichu", "Raichu"])
table.add_column("Type",["Electric", "Fire", "Water"])
table.align = "l"
print(table)