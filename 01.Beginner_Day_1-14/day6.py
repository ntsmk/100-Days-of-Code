# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Alone&url=worlds/tutorial_en/alone.json

# hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
turn_left()
move()
move()
turn_right()
move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#x = 0
#while x < 6:
#    jump()
#    x += 1

for step in range(6):
    jump()

# hurdle 2
flag = at_goal()
while flag == False:
    jump()
    flag = at_goal()

# hurdle 3
while not at_goal():
    if not front_is_clear():
        if wall_in_front():
            jump_2()
    else:
        move()

# hurdle 4
    def turn_right():
        turn_left()
        turn_left()
        turn_left()


    def jump():
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()


    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()

# final project partly code works
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        while right_is_clear():
            move()
    elif front_is_clear():
        while front_is_clear():
            move()
    else:
        turn_left()

# part 2 almost works. only 1 position does not work
    def turn_right():
        turn_left()
        turn_left()
        turn_left()


    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

# works for world1 2 & 3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

count = 0
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        count += 1
        if count > 5:
            turn_left()
            count -= 5
    elif front_is_clear():
        move()
    else:
        turn_left()