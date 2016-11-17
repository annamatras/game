import random
import sys
from termcolor import colored, cprint
import os
# Clear screen
def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def display_head():
    x = open("head.txt", "r")
    for line in x:
        cprint(line, "yellow", end='')

def display_credits():
    x = open("credits.txt", "r+")
    for line in x:
        print(line, end='')

def display_help():
    x = open("help.txt", "r+")
    for line in x:
        print(line, end='')

# def start_game():

def main():
    os.system("clear")
    while True:
        display_head()
        cprint("""
                                                      1.Play game
                                                      2.Help page
                                                      3.Credits
                                                      4.Exit
            """, attrs=['bold'])
        answer = input("What would you like to do?")
        if answer == "1":
            start_game()
        elif answer == "2":
            os.system("clear")
            display_help()
            input("\nPress any key for back to menu.")
            os.system("clear")
            main()
        elif answer == "3":
            os.system("clear")
            display_credits()
            input("\nPress any key for back to menu.")
            os.system("clear")
            main()
        elif answer == "4":
            cprint("\n Goodbye!\n", "red", attrs=['bold'])
            quit()
        elif answer != "":
            cprint("\n Wrong input. Try again!", "green")

main()
