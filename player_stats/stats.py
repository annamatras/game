import random


def user_name():
    name = input('What\'s your in game nick? (max 14 characters)')
    if len(name) > 14:
        print('Maximum 14 characters')
        user_name()
    else:
        user_name = ['User:', name]
        return user_name


def user_life(life=15, operation=0):
    life_list = ['Life:', life]
    life_list[1] = life_list[1] + (operation)
    return life_list


def stats():
    print('God of luck gave you your stats:')
    stats = inside_stats_generate()
    for i in range(len(stats)):
        print('{} {}' .format(stats[i][0], stats[i][1]))
    inside_stats_ask()
    return stats


def inside_stats_generate():
    stats = [['Str:', 10 + random.randint(0, 10)],
             ['Agi:', 10 + random.randint(0, 10)],
             ['Dex:', 10 + random.randint(0, 10)]]
    return stats


def inside_stats_ask(stats=stats):
        reroll = input('Reroll? (y/n)')
        reroll = reroll.lower()
        if reroll == 'y':
            stats()
        elif reroll == 'n':
            if condition:
                pass
            return stats
        else:
            print('Try again')
            inside_stats_ask()
