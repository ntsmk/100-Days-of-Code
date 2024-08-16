print('''
         ._.-..-._.
           | Gibson |
         0-| o    o |-0
           |        |
         0-| o    o |-0
           |        |
         0-| o    o |-0
           |        |
           '.      .'
             '____'
             |    |
             |    |
             |____|
             |    |
             |    |
             |____|
             |    |
             |    |
             |____|
             |    |
             |    |
             |----|
             |    |
             |____|
             |    |
             |____|
             |    |
             |____|
             |____|
             |____|
        _..--|____|       _
     .'      |____|      ' '
    .        |____|'.__.'   '
    :  (o)   ______         '
    '       |OOOOOO|       '
     '      |______|      '
      '                  '
       '                '
       :                :
       '                '
      '                  '
    .'       ______       '.
   '        |      |        '
  '         |OOOOOO|         '
 '          ________          '
.          (________)          .
:                              :
'           ________       o   '
 .         0________0   o      .
  .                        o  .
   .                    o    . 
    '.                     .'  Ryan S.
      '.._             _..'  Gibson Les Paul
          ^'--.....--'^ 
                8
''')
print("Welcome to music band story.")
print("Your mission is to practice at the music studio with your friends")
choice1 = input('You\'re at a shibuya scramble, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a music studio. '
                    'You are supposed to meet your friends here. '
                    'Type "wait" to wait for your friends. '
                    'Type "call" to call your friend.\n').lower()
    if choice2 == "wait":
        choice3 = input("Your friends finally arrived at the music studio. "
                        "There is 3 doors in the studio. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. What a hell?  Game Over")
        elif choice3 == "yellow":
            print("You found your room to practice. You Win!")
        elif choice3 == "blue":
            print("You enter somehow a room of monsters. Classic. Game Over.")
        else:
            print("You chose a door that doesn't even exist. Probably in 6th dimension. Game Over.")
    else:
        print("Your phone suddenly broke. Game Over.")

else:
    print("You fell in to a hole in middle of Shibuya. Game Over.")
