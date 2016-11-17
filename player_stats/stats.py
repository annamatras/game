import random


def user_name():
    name = input('What\'s your in game nick? (max 8 characters)')
    if len(name) > 8:
        print('Maximum 8 characters')
        user_name()
    else:
        return name


def user_life(life=15, operation=0):
    life_list = ['Life:', life]
    life_list[1] = life_list[1] + (operation)
    return life_list


def stats():
    print('GOD OF LUCK gave you your stats:')
    st = inside_stats_generate()
    for i in range(len(st)):
        print('{} {}' .format(st[i][0], st[i][1]))
    st = inside_stats_ask(st)
    return st


def inside_stats_generate():
    st = [['Str:', 10 + random.randint(0, 10)],
          ['Agi:', 10 + random.randint(0, 10)],
          ['Dex:', 10 + random.randint(0, 10)]]
    return st


def inside_stats_ask(st):
    reroll = input('Reroll? (y/n)')
    reroll = reroll.lower()
    if reroll == 'y':
        #  st =[]
        stats()
    elif reroll == 'n':
        if (st[0][1] > 15):
            print('So you\'re tought huh?')
            return st
        if (st[1][1] > 15):
            print('Where is my wallet?')
            return st
        if (st[2][1] > 15):
            print('So you\'re hard to kill, it seems.')
            return st
        return st
    else:
        print('Try again')
        inside_stats_ask()
print(stats())
print(user_life())
