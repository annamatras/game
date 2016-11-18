import pickle
from challenge import *
from gra import *
from stat import *

OKBLUE = '\033[94m'
FAIL = '\033[91m'
BOLD = '\033[1m'
BGGREEN ='\033[42m'
BGBLUE = '\033[44m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'
save = 0
inv = [['ruby',3,'weapon',2], ['rope',12,'others',2],['cheese',4,'food',5],
    ['shoes',1,'clothes',2], ['armor',1,'clothes',1], ['bow',1,'weapon',3],
    ['vodka',25,'others',8],['gold coin',20,'others',1],['keys', 2,'others',1]]


def add_to_inventory(inventory, items):
    """Adds loot to players inventory and returns updated inventory"""
    for item in items:
        if item in inventory:
            item[1] += 1   #if we have that item already increase number that item
        else:
            inventory.extend([item, 1, ]) # if its new item, add it to inventory
    return inventory


def print_table(inventory, stage_number, hero_name, statistics, lives, order="empty"):
    """Displays players inventory in well organised table"""
    sorted_values = []
    number_of_items = 0
    sorted_values = sorted(inventory, key=lambda inventory: inventory[2])
    print(BOLD+UNDERLINE+BGBLUE+"              I N V E N T O R Y              "+ENDC+"  ", end="")
    print(BOLD+UNDERLINE+BGBLUE+"              S T A T I S T I C              "+ENDC, end="")
    print("䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀", end="")
    print(OKBLUE)
    print("{:>10}  {:>10} {:>10} {:>10}".format("Item", "Count", "Item type", "Weight"), end="")
    print(ENDC, end="")
    print("   \033[41mSTAGE: {} \033[0m                                    ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀".format(stage_number)+ENDC, end="")
    print(ENDC)
    for i in range(45):
        print("-", end="")
    print("  "+BOLD+hero_name.upper()+ENDC+"                                     ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀")
    count = -1
    stats = []
    stats_values = []
    for index, item in enumerate(statistics):
        stats.append(statistics[index][0])
        stats_values.append(statistics[index][1])
    for item in sorted_values:
        if count <= 5:
            count += 1
        else:
            break
        print("{:>10}  {:>10} {:>10} {:>10}          {:>10}  {:>10}                ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀".format(item[0], item[1], item[2], item[3], stats[count], stats_values[count]))
    for i in range(45):
        print("-", end="")
    print("              LIVES  {:>10}".format(lives), end="")
    print("                ䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀䷀")
    print()
    for item in inventory:
        number_of_items += int(item[1])
    print("Total number of items:", number_of_items)


def display_head():
    """Displays head of boss"""
    x = open("head.txt", "r")
    for line in x:
        cprint(line, "yellow", end='')


def game_over():
    """Displays final graphs for winner"""
    os.system('clear')
    x = open("game_over.txt", "r")
    for line in x:
        cprint(line, "red", end='')
    exit()

def display_credits():
    """Displays credits"""
    x = open("credits.txt", "r+")
    for line in x:
        print(line, end='')


def display_help():
    """Displays help"""
    x = open("help.txt", "r+")
    for line in x:
        print(line, end='')


def menu():
    """Displays main menu of the game"""
    global save
    os.system("clear")
    while True:
        display_head()
        cprint("""
                                                      1.Play game
                                                      2.Help page
                                                      3.Credits
                                                      4.Load
                                                      5.Exit
            """, attrs=['bold'])
        answer = input("What would you like to do?")
        if answer == "1":
            break
        elif answer == "2":
            os.system("clear")
            display_help()
            input("\nPress any key for back to menu.")
            main()
        elif answer == "3":
            os.system("clear")
            display_credits()
            input("\nPress any key for back to menu.")
            main()
        elif answer == "4":
            # load()
            save = 1
            print(BGBLUE+BOLD+UNDERLINE, end="")
            print("LOADING SAVED GAME")
            print(ENDC, end="")
            input()
            return "load"
        elif answer == "5":
            cprint("\n Goodbye!\n", "red", attrs=['bold'])
            quit()
        elif answer != "":
            cprint("\n Wrong input. Try again!", "green")


def random_loot():
    """Generates random 3 items for player"""
    loot = random.sample(inv, 3)
    print(BGBLUE+BOLD+UNDERLINE, end="")
    print("You've found {}, {} and {}! Hit Enter".format(loot[0][0], loot[1][0], loot[2][0]))
    print(ENDC, end="")
    input()
    return loot


def getch():
    """Waits for character input from console and returns it"""
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
    """Set position of player"""
    matrix[hero_row][hero_col] = "👹"
    return matrix


def import_matrix(stage_number=1):
    """Imports map based on stage number"""
    matrix = []
    with open(str(stage_number)+".txt", "r") as handler:
        imported_data = handler.readlines()
    imported_data = [s.replace('\n', '') for s in imported_data]
    for data_row in imported_data:
        string = []
        for x in data_row:
            string.append(x)
        matrix.append(string)
    for row in range(2, len(matrix)-2):
        for col in range(2, len(matrix[0])-2):
            if random.randint(0, 200) < 2:
                matrix[row][col] = "🏆"
    return matrix


def cls():
    """Clears terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_matrix(matrix):
    """Displays map on the screen"""
    for item in matrix:
        print(''.join(item))


def stats():
    """Prints random characteristic for player toon"""
    os.system('clear')
    print('GOD OF LUCK gave you your stats:')
    print("--------------------------------")
    st = inside_stats_generate()
    for i in range(len(st)):
        print()
        print('{} {}' .format(st[i][0], st[i][1]))
    print("--------------------------------")
    st = inside_stats_ask(st)
    return st


def inside_stats_generate():
    """Generates random characteristic for player toon"""
    st = [['STRENGHT', 10 + random.randint(0, 10)],
          ['AGILITY:', 10 + random.randint(0, 10)],
          ['DEXTERITY:', 10 + random.randint(0, 10)],
          ['WILLPOWER', 10 + random.randint(0, 10)],
          ['CHARISMA', 10 + random.randint(0, 10)],
          ['WISDOM', 10 + random.randint(0, 10)],
          ['LUCK', 10 + random.randint(0, 10)],
          ['LIFES', 10 + random.randint(0, 10)]]
    return st


def inside_stats_ask(st):
    """Gives feedback for player about hes statistics and ask for reroll"""
    reroll = input('Reroll? (y/n)')
    reroll = reroll.lower()

    if reroll == 'y':
        os.system('clear')
        return stats()

    elif reroll == 'n':

        if (st[0][1] > 16):
            print('Str is over 16! So you\'re tought huh...')

        if (st[1][1] > 16):
            print('Agi is over 16! Where is my wallet...')

        if (st[2][1] > 16):
            print('Dex is over 16! So you\'re hard to kill, it seems.')

        if (st[3][1] > 16):
            print('Willpower is over 16! So you\'re resistant to psychic \
            attacks.')

        if (st[4][1] > 16):
            print('Charisma is over 16! You\'ll be alright people like you.')

        if (st[5][1] > 16):
            print('Wisdom is over 16! Profesor? smart ass huh.')

        if (st[6][1] > 16):
            print('Luck is over 16! Lucky bastard!')

        return st

    else:
        print('Try again')
        return inside_stats_ask()


def ask_name():
    """Asks player for hes name"""
    ask = "##########"
    spaces = 0
    while len(ask) > 8:
        ask = input("Type name for your character (max 8 char): ")
    spaces = 8 - len(ask)
    ask += " "*spaces
    return ask


def load(matrix, hero_name, hero_row, hero_col, statistics, inv, stage_number, lives):
    """Loads all needed parameters from file to make proper load"""
    with open("save", "rb") as handler:
        matrix = pickle.load(handler)
        hero_name = pickle.load(handler)
        hero_row = pickle.load(handler)
        hero_col = pickle.load(handler)
        statistics = pickle.load(handler)
        inv = pickle.load(handler)
        stage_number = pickle.load(handler)
        lives = pickle.load(handler)
        return matrix, hero_name, hero_row, hero_col, statistics, inv, stage_number, lives


def save_game(matrix, hero_name, hero_row, hero_col, statistics, inv, stage_number, lives):
    """Saves all needed parameters to file to make proper save"""
    with open("save", "wb") as handler:
        pickle.dump(matrix, handler)
        pickle.dump(hero_name, handler)
        pickle.dump(hero_row, handler)
        pickle.dump(hero_col, handler)
        pickle.dump(statistics, handler)
        pickle.dump(inv, handler)
        pickle.dump(stage_number, handler)
        pickle.dump(lives, handler)


def main():
    global lives
    global save
    global inv
    matrix = []
    hero_name = ""
    hero_row, hero_col = 0, 0
    statistics = []
    stage_number = 1
    lives = 0
    if save:
        (matrix, hero_name, hero_row, hero_col, statistics, inv, stage_number, lives) = load(matrix, hero_name, hero_row, hero_col, statistics, inv, stage_number, lives)
        save = 0
    else:
        matrix = import_matrix(1)
        hero_row, hero_col = 10, 5
        odp = menu()
        if odp == "load":
            main()
        hero_name = ask_name()
        statistics = stats()
        lives = statistics[7][1]
    while True:
        matrix_d = ret_matrix(matrix, hero_row, hero_col)
        print_matrix(matrix_d)
        print_table(inv, stage_number, hero_name, statistics, lives)
        char = getch()
        if (char == "a") and (matrix[hero_row][hero_col-1] != "䷀"):
            if (matrix[hero_row][hero_col-1] == "🞮"):
                stage_number += 1
                if stage_number == 4:
                    guess_game()
                    exit()
                lives = challenge(lives)
                matrix = import_matrix(stage_number)
                hero_row, hero_col = 20, 40
                continue
            if (matrix[hero_row][hero_col-1] == "🏆"):
                add_to_inventory(inv, random_loot())
            matrix[hero_row][hero_col] = " "
            hero_col -= 1
        elif (char == "d") and (matrix[hero_row][hero_col+1] != "䷀"):
            if (matrix[hero_row][hero_col+1] == "🞮"):
                stage_number += 1
                if stage_number == 4:
                    guess_game()
                lives = challenge(lives)
                matrix = import_matrix(stage_number)
                hero_row, hero_col = 20, 40
            if (matrix[hero_row][hero_col+1] == "🏆"):
                add_to_inventory(inv, random_loot())
            matrix[hero_row][hero_col] = " "
            hero_col += 1
        elif (char == "w") and (matrix[hero_row-1][hero_col] != "䷀"):
            if (matrix[hero_row-1][hero_col] == "🞮"):
                stage_number += 1
                if stage_number == 4:
                    guess_game()
                lives = challenge(lives)
                matrix = import_matrix(stage_number)
                hero_row, hero_col = 20, 40
            if (matrix[hero_row-1][hero_col] == "🏆"):
                add_to_inventory(inv, random_loot())
            matrix[hero_row][hero_col] = " "
            hero_row -= 1
        elif char == "s" and (matrix[hero_row+1][hero_col] != "䷀"):
            if (matrix[hero_row+1][hero_col] == "🞮"):
                stage_number += 1
                if stage_number == 4:
                    guess_game()
                lives = challenge(lives)
                matrix = import_matrix(stage_number)
                hero_row, hero_col = 20, 40
            if (matrix[hero_row+1][hero_col] == "🏆"):
                add_to_inventory(inv, random_loot())
            matrix[hero_row][hero_col] = " "
            hero_row += 1
        elif char == "p":
            matrix[hero_row+1][hero_col] = "🞮"
        elif char == "m":
            save_game(matrix, hero_name, hero_row, hero_col, statistics, inv, stage_number, lives)
            print(BGBLUE+BOLD+UNDERLINE, end="")
            print("SAVING GAME ... Enter")
            print(ENDC, end="")
            input()
            main()
        elif (char == "q"):
            exit()
        else:
            pass

if __name__ == "__main__":
    main()
