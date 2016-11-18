import random
import sys
from termcolor import colored, cprint
import os

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

def menu():
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
            break
        elif answer == "2":
            os.system("clear")
            display_help()
            input("\nPress any key for back to menu.")
            menu()
        elif answer == "3":
            os.system("clear")
            display_credits()
            input("\nPress any key for back to menu.")
            menu()
        elif answer == "4":
            cprint("\n Goodbye!\n", "red", attrs=['bold'])
            quit()
        elif answer != "":
            cprint("\n Wrong input. Try again!", "green")
