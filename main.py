import os
import art

def add(n1, n2):
    return n1 + n2

def multiply(n1,n2) :
    return n1 * n2

def subtract(n1, n2) :
    return n1 - n2

def divide(n1, n2) :
    return n1 / n2

operation = {
    "+" : add,
    "*" : multiply,
    "-" : subtract,
    "/" : divide
}

print(art.logo)
continue_calculate = True
result = 0.0
first_number = int(input("what is the first number?\n"))

operate = input("+\n-\n*\n/\nPick an operation\n")

second_number = int(input("what is the next number?\n"))

result = operation[operate](first_number,second_number)

print(f"result : {result}")

while continue_calculate :
    ask_to_continue = input(f"type 'y' to continue calculating with {result} or type 'n' to start a new calculater\n").lower()
    if ask_to_continue == "y" :
        first_number = result
        operate = input("+\n-\n*\n/\nPick an operation\n")
        second_number = int(input("what is the next number?\n"))
        result = operation[operate](first_number,second_number)
        print(f"result : {result}")
    if ask_to_continue == "n" :
        os.system("cls")
        first_number = int(input("what is the first number?\n"))

        operate = input("+\n-\n*\n/\nPick an operation\n")

        second_number = int(input("what is the next number?\n"))

        result = operation[operate](first_number, second_number)

        print(f"result : {result}")
