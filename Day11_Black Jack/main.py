import random
import art
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True
while continue_game :
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()

    if start_game == "y" :
        os.system("cls")
        print(art.logo)
        player_cards=[]
        player_first_card=random.choice(cards)
        player_second_card=random.choice(cards)
        player_cards.append(player_first_card)
        player_cards.append(player_second_card)
        score = sum(player_cards)
        print(f"your cards : {player_cards}, current score : {score}")
        if score == 21 :
            print("you get Black Jack! You win!")


        computer_cards=[]
        computer_first_card=random.choice(cards)
        computer_cards.append(computer_first_card)
        computer_score=sum(computer_cards)
        print(f"computer's first card : {computer_first_card}")



        while score < 21 :
            get_another_card = input("Type 'y' to get another card, type 'n' to pass\n").lower()
            if get_another_card == "y" :
                player_cards.append(random.choice(cards))
                score=sum(player_cards)
                if score > 21 :
                    if 11 in player_cards :
                        player_cards[player_cards.index(11)] = 1
                        score = sum(player_cards)
                    else :
                        print(f"your cards : {player_cards}, final score : {score}\nyou went over. you lose")
                        break
                elif score == 21 :
                    print(f"your final hand : {player_cards}, final score : {score}\n"
                          f"you get Black Jack! You Win!")
                    break
                print(f"your cards : {player_cards}, current score : {score}\n"
                      f"computer's first card : {computer_first_card}")
            elif get_another_card == "n" :
                print(f"your final hand : {player_cards}, final score : {score}")
                while computer_score <= 17 :
                    computer_cards.append(random.choice(cards))
                    computer_score = sum(computer_cards)
                    if computer_score > 21 :
                        if 11 in computer_cards :
                            computer_cards[computer_cards.index(11)] = 1
                            computer_score = sum(computer_cards)

                if computer_score > 21 :
                    print(f"computer cards : {computer_cards}, final score : {computer_score}\n "
                          f"opponent went over! You Win!")
                elif computer_score == 21 :
                    print(f"computer cards : {computer_cards}, final score : {computer_score}\n"
                          f"opponent get Black Jack! You lose")
                elif score > computer_score :
                    print(f"computer's hand : {computer_cards}, final score : {computer_score}\n"
                          f"you win")
                elif score == computer_score :
                    print(f"computer's hand : {computer_cards}, final score : {computer_score}\n"
                          f"draw")
                else :
                    print(f"computer's hand : {computer_cards}, final score : {computer_score}\n"
                          f"you lose")
                break

    if start_game == "n" :
        continue_game = False
        os.system("pause")

