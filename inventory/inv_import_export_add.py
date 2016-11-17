import csv


inv = {}
inv_add = {}


def import_inventory(inventory, filename='import_inventory.csv'):

    '''Imports a dictionary from a file'''
    try:
        with open(filename, mode='r') as in_file:
            next(in_file)  # Starts from second row in the file
            reader = csv.reader(in_file)
            inventory = {rows[0]: [rows[1], rows[2], rows[3]]
                         for rows in reader}
            return inventory
    except FileNotFoundError as e:
        print('There is no file: {} in your directory\
, please create your import file. See you next time! ' .format(filename))
        quit()


def export_inventory(inventory, filename='import_inventory.csv'):
    '''Writes to file - make sure not to change position, of values
        dependancy def: add_to_inventory, import_inventory'''
    first_row_item_name = 'item_name'
    first_row_item_count = 'count'
    first_row_item_type = 'type'
    first_row_item_weight = 'weight'

    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE, escapechar=',')
        writer.writerow([first_row_item_name, first_row_item_count,
                        first_row_item_type, first_row_item_weight])
        for key, value in inventory.items():
            writer.writerow([key, value[0], value[1], value[2]])


def add_to_inventory(inventory, type_var, filename='import_inventory.csv'):
    ''' 1. Imports a items list from a file
        2. Randomly picks an item of a type provided
        3. Assigns(add) new values to inventory item equal to item from list'''
    try:
        with open(filename, mode='r') as in_file:
            next(in_file)  # Starts from second row in the file
            reader = csv.reader(in_file)
            inv_add = []
            for rows in reader:
                # if ((type([rows[0]) is not str) or (type([rows[1]) is not int) or (type([rows[2]) is not str) or (type([rows[3]) is not int)):
                #     print('Seems like type of an value in {}, {} row is incorrect' .format(filename, rows))
                #     print('Program will shut down automatically but will try to save your game')
                #     quit()
                if ('{}'.format(rows[2])) == type_var:  # random type item pick
                    inv_add = [rows[0], rows[1], rows[2], rows[3]]
                    for key, value in inventory.items():
                        if key == inv_add[0]:  # add one item to dictionary
                            inventory[key] = [int(value[0]) + int(inv_add[1]), value[1], int(value[2]) + int(inv_add[3])]
                            return inventory
    except FileNotFoundError as e:
        print('There is no file: {} in your directory\
              , please create your import file. See you next time! '
              .format(filename))
        quit()


inv = import_inventory(inv)
print(inv)
inv = add_to_inventory(inv, 'Other')
print(inv)
export_inventory(inv)
