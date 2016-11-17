#xterm -fullscreen -e python3 script.py
import random
OKBLUE = '\033[94m'
FAIL = '\033[91m'
BOLD = '\033[1m'
BGGREEN ='\033[42m'
BGBLUE = '\033[44m'
ENDC = '\033[0m'
UNDERLINE = '\033[4m'
#inv = {'rope': 1, 'torch': 3, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = [['ruby',3,'weapon',2], ['rope',12,'others',2],['cheese',4,'food',5],
    ['shoes',1,'clothes',2], ['armor',1,'clothes',1], ['bow',1,'weapon',3],
    ['vodka',25,'others',8],['gold coin',20,'others',1],['keys', 2,'others',1]]
#loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    """ Displays player inventory names and quantities"""
    number_of_items = 0
    print("Inventory:")
    for item, value in inventory.items():
        print(value, item)
        number_of_items += value
    print("Number of items: %d" % number_of_items)


def add_to_inventory(inventory, items):
    """Adds loot to players inventory and returns updated inventory"""
    for item in items:
        if item in inventory:
            item[1] += 1   #if we have that item already increase number that item
        else:
            inventory.extend([item, 1, ]) # if its new item, add it to inventory
    return inventory


def print_table(inventory, order="empty"):
    """Displays players inventory in well organised table"""
    sorted_values = []
    number_of_items = 0
    sorted_values = sorted(inventory, key=lambda inventory: inventory[2])
    print(BOLD+UNDERLINE+BGBLUE+"              I N V E N T O R Y              "+ENDC+"  ", end="")
    print(BOLD+UNDERLINE+BGBLUE+"              S T A T I S T I C              "+ENDC, end="")
    print("‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡", end="")
    print(OKBLUE)
    print("{:>10}  {:>10} {:>10} {:>10}".format("Item", "Count", "Item type", "Weight"), end="")
    print(ENDC, end="")
    print("   \033[41mSTAGE: {} \033[0m                                    ‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡".format(stage_number)+ENDC, end="")
    print(ENDC)
    for i in range(45):
        print("-", end="")
    print("  "+BOLD+"RODERICK"+ENDC+"                                     ‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡")
    count = -1
    stats = ["STRENGHT", "WILLPOWER", "WISDOM", "DEXTERITY", "CONDITION", "CHARISMA","SOCIAL"]
    stats_values = [12, 2, 4, 14, 16, 13, 10]
    for item in sorted_values:
        if count <= 5:
            count += 1
        else:
            break
        print("{:>10}  {:>10} {:>10} {:>10}          {:>10}  {:>10}                ‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡".format(item[0], item[1], item[2], item[3], stats[count], stats_values[count]))
    for i in range(45):
        print("-", end="")
    print("              LIVES  {:>10}".format(lives), end="")
    print("                ‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡")
    print()
    for item in inventory:
        number_of_items += int(item[1])
    print("Total number of items:", number_of_items)


def import_inventory(inventory, filename="import_inventory.csv"):
    """Imports inventory from file and updates it with current inventory"""
    number_of_items = 0
    with open(filename, "r", encoding="utf-8") as handler:
        items_list = handler.readlines()
        del items_list[0]  #item_name, counts - descriptive first line of file
    for item in items_list:
        str_without_newline = item.replace("\n","")
        splitted_list = str_without_newline.split(",")
        key = splitted_list[0]
        if splitted_list[1].isdigit():
            value = int(splitted_list[1])
        else:
            print("Problem with parsing {}.".format(filename))
            exit()
        if key in inventory:
            inventory[key] = int(inventory[key])+int(value)
            continue
        to_add=(key, value)
        inventory.update([to_add])
    print("\nInventory:\n")
    for key, value in inventory.items():
        print(key, value)
    for item in inventory.values():
        number_of_items += item
    print("Total number of items: ", number_of_items)


def export_inventory(inventory, filename="import_inventory.csv"):
    """Exports current inventory to file"""
    with open(filename, "w", encoding="utf-8") as handler:
        handler.write("item_name,count\n")
        for key, value in inventory.items():
            handler.write(key+","+str(value)+"\n")

def random_loot():
    loot = random.sample(inv,3)
    print(BGBLUE+BOLD+UNDERLINE, end="")# print(BGBLUE, end="")
    print("You've found {}, {} and {}! Hit Enter".format(loot[0][0], loot[1][0], loot[2][0]))
    print(ENDC, end="")
    input()
    return loot

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

def random_start():
    positionx = random.randint(150)
    positiony = random.randint(10)+30
    return positionx, positiony

hero_row, hero_col = 10, 5
lives = 10
stages = []
stage_number = 1
matrix = import_matrix(1)
#import_inventory(inv)
while True:
    matrix_d = ret_matrix(matrix, hero_row, hero_col)
    print_matrix(matrix_d)
    print_table(inv)
    char = getch()
    if (char == "a") and (matrix[hero_row][hero_col-1] != "‡"):
        if (matrix[hero_row][hero_col-1] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
            continue
        if (matrix[hero_row][hero_col-1] == "█"):
            add_to_inventory(inv, random_loot())
        matrix[hero_row][hero_col] = " "
        hero_col -= 1
    elif (char == "d") and (matrix[hero_row][hero_col+1] != "‡"):
        if (matrix[hero_row][hero_col+1] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
        if (matrix[hero_row][hero_col+1] == "█"):
            add_to_inventory(inv, random_loot())
        matrix[hero_row][hero_col] = " "
        hero_col += 1
    elif (char == "w") and (matrix[hero_row-1][hero_col] != "‡"):
        if (matrix[hero_row-1][hero_col] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
        if (matrix[hero_row-1][hero_col] == "█"):
            add_to_inventory(inv, random_loot())
        matrix[hero_row][hero_col] = " "
        hero_row -= 1
    elif char == "s" and (matrix[hero_row+1][hero_col] != "‡"):
        if (matrix[hero_row+1][hero_col] == "E"):
            stage_number += 1
            matrix = import_matrix(stage_number)
            hero_row, hero_col = 20, 40
        if (matrix[hero_row+1][hero_col] == "█"):
            add_to_inventory(inv, random_loot())
        matrix[hero_row][hero_col] = " "
        hero_row += 1
    elif char == "p":
        matrix[hero_row+1][hero_col] = "E"
    elif (char == "q"):
        break
    else:
        pass
