rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
my_choice =int(input('What do you choose? Type "0" for Rock, "1" for Scissors, "2" for Paper'))
RSP = [rock, scissors, paper]

import random
computer_choice=random.randint(0,2)
if my_choice == 0 :
    print(RSP[0])
    print("computer choose :")
    print(RSP[computer_choice])
    if computer_choice == 0 :
        print("DRAW")
    elif computer_choice == 1 :
        print("WIN")
    else :
        print("LOSE")
elif my_choice == 1 :
    print(RSP[1])
    print("computer choose :")
    print(RSP[computer_choice])
    if computer_choice == 0 :
        print("LOSE")
    elif computer_choice == 1 :
        print("DRAW")
    else :
        print("WIN")
elif my_choice == 2 :
    print(RSP[2])
    print("computer choose :")
    print(RSP[computer_choice])
    if computer_choice == 0 :
        print("WIN")
    elif computer_choice == 1 :
        print("LOSE")
    else :
        print("DRAW")
else :
    print("You Typed Wrong Number. Play Again")

