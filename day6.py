# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Alone&url=worlds/tutorial_en/alone.json

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