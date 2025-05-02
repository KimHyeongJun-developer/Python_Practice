# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import os
import art
print(art.logo)

bid_information = {}

bid_continue = True

while bid_continue :
    name = input("what is your name?")
    price = int(input("what is your bid?($)"))
    bid_information[name]=price
    other_person = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if other_person == "yes" :
        os.system("cls")
    elif other_person == "no" :
        bid_continue = False

candidate = ""
candidate_price = 0
for key in bid_information :
    if bid_information[key] > candidate_price :
        candidate = key
        candidate_price = bid_information[key]

print(f"The winner is {candidate} for {candidate_price}$")
os.system("pause")