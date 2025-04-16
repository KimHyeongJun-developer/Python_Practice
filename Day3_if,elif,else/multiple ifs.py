print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
fee=0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        fee = 5
    elif age <= 18:
        fee = 7
    else:
        fee = 9
    photo = input("Do you want photos?(yes or no)")
    if photo == "yes" :
        fee += 3
    print(f"your total fee is {fee}$")
else :
    print("Sorry you have to grow taller before you can ride.")
