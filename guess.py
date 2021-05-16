
import random

no= random.randint(0,20)

def easy_mode():
        print(">.< PLEASE GUESS THE NUMBER >.<")

        try:
            user_guess = int(input(">"))

            if user_guess == no:
                print("\n~You have won, but at what cost~")

            elif user_guess > no:
                print("~You went higher than the actual answer~\n")
                easy_mode()

            elif user_guess < no:
                print("~You went lower than the actual answer~\n")
                easy_mode()

        except ValueError:
            print(">.< Please enter a number >.<")


def hard_mode():
    print(">.< PLEASE GUESS THE NUMBER >.<")
    try:

     tries=0
     while tries<5:
        user_guess=int(input(">"))

        if user_guess == no:
            print("\n~You have won, but at what cost~")
            exit()

        elif user_guess > no:
            print("~You went higher than the actual answer~\n")
            tries+=1
            if tries==5:
                print(f'\n You failed in guessing the right number! :(,You had {tries} tries')
            else:
                print('>.< Please enter a number >.<')
        elif user_guess < no:
            print("~You went lower than the actual answer~\n")
            tries += 1
            if tries == 5:
                print(f'\n You failed in guessing the right number! :(,You had {tries} tries')
            else:
                print('>.< Please enter a number >.<')
    except ValueError:
        print('>.< Please enter a number >.<')

def pre_game():
    print("So, How would you like to play? Easy or Hard?")
    print("~1 for Easy and 2 for Hard. Press 3 for HELP~")
    oper = input(">")
    if oper == '1':
        easy_mode()
    elif oper == '2':
        hard_mode()
    if oper == '3':
        print("\n~In Easy mode you have unlimited tries.~\n ~And in Hard mode, you only have 5 tries.~\n")
        pre_game()

pre_game()


