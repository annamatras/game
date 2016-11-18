import random
import os
from termcolor import colored, cprint

def try_again():
    again = 'y'
    while again == 'y' or again == 'Y':
        again = input('Would you like to play again?')
        if again == 'y' or again == 'Y':
            return True
        else:
            exit()


def game_over():
    """Displays final graphs for winner"""
    os.system('clear')
    x = open("game_over.txt", "r")
    for line in x:
        cprint(line, "red", end='')
    print("You win this time, poor mortal. Now you can take all my gold!")
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
    number_str = ""
    for i in number:
        number_str = str(number_str) + str(i)

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
            print("My secret code was ", number)
            print("You are doomed now!!! ")
            input()
            exit()
        elif answer == number_str:
            game_over()
            input()
            exit()
