import csv
inv = {}


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


def export_inventory(inventory, filename='export_inventory.csv'):
    '''Writes to file'''
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

inv = import_inventory(inv)
export_inventory(inv)
