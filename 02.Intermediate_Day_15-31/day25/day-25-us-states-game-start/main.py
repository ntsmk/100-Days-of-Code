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
state_list = data.state.to_list()
correct_list = []

isCorrect = False
isGameon = True


# take input and see if it matches among the 50 states list
def check_state(answer):
    if answer in state_list:
        return True
    else:
        return False


# keep guessing by using a loop until the end
while isGameon:
    answer_state = screen.textinput(title=input_title, prompt="What's another state?").title()

    # if matches, the word goes to x and y. increase the score (states)
    if check_state(answer_state):
        correct_state = data[data.state == answer_state]
        correct_list.append(correct_state.state.to_string(index=False, header=False))

        name = correct_state.state.to_string(index=False, header=False)
        x = int(correct_state.x.iloc[0])
        y = int(correct_state.y.iloc[0])
        score.update_state(name, x, y)

    print(correct_list)

    # todo count the score xx /50 states correct and show it on the title
    if len(correct_list) != 0:
        score.show_scores()

# when you answer every state, the game ends
    if correct_list == state_list:
        isGameon = False
