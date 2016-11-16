
my_dict = {'ruby': [3, 'Clothes', 3], 'rope': [8, 'Clothes', 5],
           'potion': [9, 'Other', 5], 'pot': [9, 'Other', 5], 'por': [9, 'Other', 5], 'ion': [9, 'Other', 5]}

user_name = ['User:', 'Sebastian']
user_life = ['Life:', 15]
user_time_left = ['Time Left:', 50]

len(str(print("{:<15} {:<15} | {:<10} {:<10} {:<10} {:<10}".format('Stats:', '',
    'Item Name', 'Item count', 'Weight', 'Type'))))

print("{:=<15} {:=<15} | {:=<10} {:=<10} {:=<10} {:=<10}" .format("", "", "", "", "", ""))

i = 1
for key, value in my_dict.items(), :
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

#http://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary
#http://stackoverflow.com/questions/19916861/how-can-i-print-a-dictionary-in-table-format
#http://stackoverflow.com/questions/16189546/print-out-dictionary-in-a-table-format
#http://stackoverflow.com/questions/14993049/how-to-format-a-dict-of-lists-as-a-table


#http://stackoverflow.com/questions/7392779/is-it-possible-to-print-a-string-at-a-certain-screen-position-inside-idle
