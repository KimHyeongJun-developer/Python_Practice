import random
import art
import os
print(art.logo)

goal_number=random.randint(1,100)

print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard : ").lower()

def guess(num) :
    attempts=num
    while attempts >0 :
        guess_number = int(input("Make a guess : "))
        if attempts == 1 :
            if guess_number < goal_number:
                print("You've run out of guesses.")
                attempts -= 1
            elif guess_number > goal_number:
                print("You've run out of guesses..")
                attempts -= 1
            else:
                print(f"You got it.")
                break
        else :
            if guess_number < goal_number :
                print("Too low.\nGuess again.")
                attempts -= 1
                print(f"you have {attempts} times to guess number")
            elif guess_number > goal_number :
                print("Too high.\nGuess again.")
                attempts -= 1
                print(f"you have {attempts} times to guess number")
            else :
                print("You got it.")
                break

if difficulty == "easy" :
    guess(10)
else :
    guess(5)

os.system("pause")