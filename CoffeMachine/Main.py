MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}
profit = 0

def check_ingredient(product) :
    for i in resources :
        if resources[i] < MENU[product]["ingredients"][i] :
            print(f"Sorry We don't have Enough {i}")
            return False
    return True

def check_money() :
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

coffee_order = True
while coffee_order == True :
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report" :
        print(f"water : {resources["water"]}")
        print(f"milk : {resources["milk"]}")
        print(f"coffee : {resources["coffee"]}")

    elif order == "off" :
        break

    elif order == "espresso" or "latte" or "cappuccino" :
        if check_ingredient(order) == True :
            if check_money() >= MENU[order]["cost"] :
                profit += MENU[order]["cost"]
                for i in resources:
                    resources[i] -= MENU[order]["ingredients"][i]
                print(resources)
                print(profit)
                print(f"Here is your {order}. Enjoy!")
            else :
                print("Sorry, That's not enough money. Money Refunded")
                coffee_order = False
    else :
        print("Error Caused! Try again")

    ask_another_coffee = input("Do you need another one? (yes/no) : ").lower()
    if ask_another_coffee == "no" :
        coffee_order = False





