
def game_over():

    x = open("game_over.txt", "r")
    for line in x:
        cprint(line, "red", attrs=[bold], end='')
