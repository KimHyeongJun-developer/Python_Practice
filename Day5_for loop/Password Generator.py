letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

password_list = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for i in range(int(nr_letters)) :
    password_list.append(random.choice(letters))

nr_symbols = int(input(f"How many symbols would you like?\n"))
for i in range(int(nr_symbols)) :
    password_list.append(random.choice(symbols))

nr_numbers = int(input(f"How many numbers would you like?\n"))
for i in range(int(nr_numbers)) :
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for i in password_list :
    password += i

print(f"Your Password Is {password}")



