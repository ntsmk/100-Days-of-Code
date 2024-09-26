import turtle
import pandas
from score import Score

screen = turtle.Screen()
screen.title("US states Game")
input_title = "Guess the State"

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

score = Score()


# read CSV file 50_states.csv
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct_list = []

isCorrect = False
isGameon = True

# take input and see if it matches among the 50 states list
def check_state(answer):
    if answer in state_list:
        return True
    else:
        return False


# keep guessing by using a loop
while isGameon:
    answer_state = screen.textinput(title=input_title, prompt="What's another state?").title()
    print(check_state(answer_state))

# todo if matches, the word goes to x and y. increase the score (states)
    if check_state(answer_state):
        correct_state = data[data.state == answer_state]
        correct_list.append(correct_state.state)

        # name = correct_state.state
        # x = correct_state.x
        # y = correct_state.y
        score.update_state("Alabama", 139 , -77)


# todo count the score xx /50 states correct and show it on the title
        print(correct_list)




