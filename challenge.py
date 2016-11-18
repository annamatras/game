import random
import os
from termcolor import colored, cprint

def get_input():
    global my_number
    print(rand)
    my_number = int(input("What is your quess? "))


def die():
    print("You are dead!")
    exit()

def check_number(lives):
    global my_number
    global rand
    #global lives
    if my_number == rand:
        print('\nYES!!! {} is my secret number. Gratulation!\n'.format(
                                                            my_number))
        input()
        return "won"
        # again = input("Would you like to play the game once again? (y/n)")
        # if again == 'y':
        #     main()
        # else:
        #     input("Press any key to exit program")
        #     os.system('clear')
        #     quit()
    elif my_number < rand:
        lives -= 1
        if lives < 1:
            die()
        print('=> {} is too low\n'.format(my_number))
        input("Enter")
    elif my_number > rand:
        lives -= 1
        if lives < 1:
            die()
        print('=> {} is too high\n'.format(my_number))
        input("Enter")
    return lives

my_number = 0
print("\n\nWelcome in **Coding Dojo special** game!")


def challenge(lives):
    #global lives

    global user_name
    global rand
    rand = random.randrange(1, 30)
    print("I'm thinking of a number between 1 and 30.\n")

    #  print(rand)
    while True:
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
        print("LIVES", lives)
        if lives < 1:
            die()
        get_input()
        guessed = check_number(lives)
        if guessed == "won":
            return lives
        else:
            lives = guessed


# if __name__ == '__main__':
#     main()
