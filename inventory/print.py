

my_dict = {'ruby': [3, 'Clothes', 3], 'rope': [8, 'Clothes', 5],
           'potion': [9, 'Other', 5]}

print ("{:<10} {:<10} {:<5}".format('Key', 'Label', 'Number'))

for key, value in my_dict.items():
    print ("{:<10} {:<10} {:<5}".format(key, value[0], value[1]))

#http://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary
#http://stackoverflow.com/questions/19916861/how-can-i-print-a-dictionary-in-table-format
#http://stackoverflow.com/questions/16189546/print-out-dictionary-in-a-table-format
#http://stackoverflow.com/questions/14993049/how-to-format-a-dict-of-lists-as-a-table
