import turtle
import pandas

screen = turtle.Screen()
screen.title("US states Game")
input_title = "Guess the State"

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)





# todo read CSV file 50_states.csv
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct_list = []

# todo take input and see if it matches among the 50 states list
isCorrect = False
isGameon = True
while isGameon:
    answer_state = screen.textinput(title=input_title, prompt="What's another state?").title()
    for state in state_list:
        if state == answer_state:
            isCorrect = True
        else:
            isCorrect = False

    # print(isCorrect)

    # todo if matches, the word goes to x and y. increase the score (states)
    correct_state = data[data.state == answer_state]
    # print(int(correct_state.x), int(correct_state.y))

    # if not matches, nothing happens,

    # todo count the score xx /50 states correct and show it on the title
    correct_list.append(str(correct_state.state))
    if answer_state not in state_list:
        isGameon = False

print(correct_list)

