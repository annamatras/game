import random
import os
from termcolor import colored, cprint

os.system('clear')  # clear screen
cprint("""

        From time to time in our life appears...

           ______________________________________
  ________|                                      |_______
  \       |           CODING DOJO                |      /
   \      |            challenge                 |     /
   |      |______________________________________|     |
  |__________)                                (_________|


            TIME TO IMPROVE YOUR CODING SKILLS!
       GUESS SECRET NUMBER AND GO TO THE NEXT LEVEL!

    """, "yellow", attrs=['bold'])

def get_input():
    global my_number
    my_number = int(input("What is your quess? "))


def check_number():
    global my_number
    global rand
    if my_number == rand:
        print('\nYES!!! {} is my secret number. Gratulation!\n'.format(
                                                            my_number))
        again = input("Would you like to play the game once again? (y/n)")
        if again == 'y':
            main()
        else:
            input("Press any key to exit program")
            os.system('clear')
            quit()
    elif my_number < rand:
        print('=> {} is too low\n'.format(my_number))
    elif my_number > rand:
        print('=> {} is too high\n'.format(my_number))


my_number = 0
print("\n\nWelcome in **Coding Dojo scpecial** game!")


def main():
    global user_name
    global rand
    rand = random.randrange(1, 30)
    print("I'm thinking of a number between 1 and 30.\n")

    #  print(rand)
    while True:
        get_input()
        check_number()

if __name__ == '__main__':
    main()
