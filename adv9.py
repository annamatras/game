#xterm -fullscreen -e python3 script.py
import random
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


def ret_matrix(matrix, hero_row, hero_col):
    matrix[hero_row][hero_col] = "@"
    return matrix

def import_matrix(stage_number=1):
    matrix = []
    with open(str(stage_number)+".txt","r") as handler:
        imported_data = handler.readlines()
    imported_data = [s.replace('\n', '') for s in imported_data]
    for data_row in imported_data:
        string = []
        for x in data_row:
            string.append(x)
        matrix.append(string)
    for row in range(2, len(matrix)-2):
        for col in range(2, len(matrix[0])-2):
            if random.randint(0,200)<2:
                matrix[row][col] = "█"
    return matrix

def cls():
    """Clears terminal"""
    os.system('cls' if os.name=='nt' else 'clear')

def print_matrix(matrix):
    for item in matrix:
        print(''.join(item))

hero_row, hero_col = 10, 5
stages = []
stage_number = 1
matrix = import_matrix(1)
while True:
    matrix_d = ret_matrix(matrix, hero_row, hero_col)
    print_matrix(matrix_d)



    my_dict = {'ruby': [3, 'Clothes', 3], 'rope': [8, 'Clothes', 5],
           'potion': [9, 'Other', 5], 'pot': [9, 'Other', 5], 'por': [9, 'Other', 5], 'ion': [9, 'Other', 5],
           'gold coin': [6, 'Other', 5], 'Sword': [1, 'Other', 10], 'vodka': [100,'Other', 15],
           'old bread': [3,'Other', 2], 'Stinky cheese': [2,'Other',1]}

    user_name = ['User:', 'Sebastian']
    user_life = ['Life:', 15]
    user_time_left = ['Time Left:', 50]

    len(str(print("{:<15} {:<15} | {:<10} {:<10} {:<10} {:<10}".format('Stats:', '',
        'Item Name', 'Item count', 'Weight', 'Type'))))

    print("{:=<15} {:=<15} | {:=<10} {:=<10} {:=<10} {:=<10}" .format("", "", "", "", "", ""))

    i = 1
    for key, value in my_dict.items():
        i += 1

        if i == 2:
            print ("{:<15} {:<15} | {:<10} {:<10} {:<10} {:<10}".format(user_name[0], user_name[1], key, value[0], value[2], value[1]))
            i += 1
            continue
        elif i == 4:
            print ("{:<15} {:<15} | {:<10} {:<10} {:<10} {:<10}".format(user_life[0], user_life[1], key, value[0], value[2], value[1]))
            i += 1
            continue
        elif i == 6:
            print ("{:<15} {:<15} | {:<10} {:<10} {:<10} {:<10}".format(user_time_left[0], user_time_left[1], key, value[0], value[2], value[1]))
            i += 1
            continue
        else:
            print ("{:<15} {:<15} | {:<10} {:<10} {:<10} {:<10}".format(' ', ' ', key, value[0], value[2], value[1]))





    char = getch()
    if (char == "a") and (matrix[hero_row][hero_col-1] != "‡"):
        if (matrix[hero_row][hero_col-1] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
            continue
        matrix[hero_row][hero_col] = " "
        hero_col -= 1
    elif (char == "d") and (matrix[hero_row][hero_col+1] != "‡"):
        if (matrix[hero_row][hero_col+1] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
        matrix[hero_row][hero_col] = " "
        hero_col += 1
    elif (char == "w") and (matrix[hero_row-1][hero_col] != "‡"):
        if (matrix[hero_row-1][hero_col] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
        matrix[hero_row][hero_col] = " "
        hero_row -= 1
    elif char == "s" and (matrix[hero_row+1][hero_col] != "‡"):
        if (matrix[hero_row+1][hero_col] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
        matrix[hero_row][hero_col] = " "
        hero_row += 1
    elif (char == "q"):
        break
    else:
        pass
