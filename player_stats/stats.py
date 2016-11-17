import random


def user_name():
    name = input('What\'s your in game nick? (max 8 characters)')
    if len(name) > 8:
        print('Maximum 8 characters')
        user_name()
    else:
        return name


def user_life(life=15, operation=0):
    life_list = ['LIFE:', life]
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
    st = [['STRENGHT', 10 + random.randint(0, 10)],
          ['AGILITY:', 10 + random.randint(0, 10)],
          ['DEXTERITY:', 10 + random.randint(0, 10)],
          ['WILLPOWER', 10 + random.randint(0, 10)],
          ['CHARISMA', 10 + random.randint(0, 10)],
          ['WISDOM', 10 + random.randint(0, 10)],
          ['LUCK', 10 + random.randint(0, 10)],
          ['LIFE', 15 + random.randint(0, 10)]]
    return st


def inside_stats_ask(st):
    reroll = input('Reroll? (y/n)')
    reroll = reroll.lower()

    if reroll == 'y':
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
# print(stats())
# print(user_life())
