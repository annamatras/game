import random
print("""
I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:

When I say:	That means:

  Cold	   No digit is correct.

  Warm     One digit is correct but in the wrong position.

  Hot      One digit is correct and in the right position.

I have thought up a number. You have 10 guesses to get it.
""")


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
        # print('Comparing user %s with secret %s' % (user_number, secret))
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
    number = [1, 2, 3]
    print(number)

    while user_numbers != number:
        count += 1
        user_nr = []
        secret_nr = []
        results = []
        answer = input("Guess #%d:" % count)
        user_numbers = [int(answer[0]), int(answer[1]), int(answer[2])]

        for user_number in user_numbers:
            results.append(check_number(user_number, user_numbers, number))

        print_results(results)

        if count == 10:
            print("You have no more guesses!")
            try_again()

    print("Number:", number)


guess_game()
