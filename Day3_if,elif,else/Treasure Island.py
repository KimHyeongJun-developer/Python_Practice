print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input('You are at a cross road.'
                     'Where do you want to go?'
                     'Type "left" or "right"').lower()
if first_choice == "left" :
    second_choice=input('You\'ve come to a lake. '
                        'There is an island in the middle of the lake. '
                        'Type "wait" to wait for a boat or Type "swim" to go to island').lower()
    if second_choice=="wait" :
        third_choice = input('you found three doors.'
                             'there are "red","yellow", and "blue" doors.'
                             'which door will you get into?').lower()
        if third_choice == "yellow" :
            print("Congratulations! You Win!")
        elif third_choice == "red" :
            print("you are burnt by fire. Game Over")
        elif third_choice == "blue" :
            print("You are eaten by beasts. Game Over")
        else :
            print("You are stupid. Game Over")
    elif second_choice == "swim" :
        print("You are attacked by  trout. Game Over")
    else :
        print("You are stupid. Game Over")
else : print("You fall into a hole. Game Over")