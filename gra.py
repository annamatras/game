import random
import os
from termcolor import colored, cprint


os.system('clear')

cprint("""
                VERY SCARY GUESS NUMBER GAME


""", "red", attrs=['bold'])



cprint("""
                            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      /
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `//  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  //`\ |  |  | /,//' \,'  /
            /   /     ||--+--|--+-/-|     \   /
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'

""", "yellow", attrs=['bold'])

cprint("""
If you want to pass you codecool exams, try with me!
Guess the number and complet you education...
""", "red", attrs=['bold'])

cprint("""I am thinking of a 3-digit number. Try to guess what it is.

  Hot      One digit is correct and in the right position.
  Warm     One digit is correct but in the wrong position.
  Cold	   Digit is not correct.

I have thought up a number. You have 10 guesses to get it.
""", "yellow", attrs=['bold'])


def try_again():
    again = 'y'
    while again == 'y' or again == 'Y':
        again = input('Would you like to play again?')
        if again == 'y' or again == 'Y':
            return True
        else:
            exit()


def check_number(user_number, user_numbers, secrets):
    for secret in secrets:
        if user_number == secret:
            if user_numbers.index(user_number) == secrets.index(secret):
                return "Hot"
            else:
                return "Warm"

    return "Cold"


def print_results(results):
    # print('Results ', results)
    for result in results:
        if result == 'Hot':
            print(result, " ", end="")

    for result in results:
        if result == 'Warm':
            print(result, " ", end="")

    for result in results:
        if result == 'Cold':
            print(result, " ", end="")
    print("")


def guess_game():
    number = []
    user_numbers = []
    answer = ""
    count = 0
    while len(number) < 3:
        digit = random.randint(0, 9)
        if (digit == 0 and len(number) < 1) or (digit in number):
            continue
        else:
            number.append(digit)
    print(number)

    while answer != number:
        count += 1
        user_nr = []
        results = []
        answer = input("Guess #%d:" % count)
        user_numbers = [int(answer[0]), int(answer[1]), int(answer[2])]

        for user_number in user_numbers:
            results.append(check_number(user_number, user_numbers, number))
        print_results(results)

        if count == 10:
            print("You have no more guesses!")
            print("Number:", number)
            try_again()

        else:
            print("Win!")
            count = 0
            try_again()

guess_game()
