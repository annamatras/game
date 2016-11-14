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


def ret_matrix(x_coord, y_coord, x=30, y=30):
    matrix = []
    for row in range(x):
        matrix.append([])
        for col in range(y):
            if row == 0 or row == x-1 or col == 0 or col == y-1:
                matrix[row].append('X')
            else:
                matrix[row].append('.')
        matrix[y_coord][x_coord] = "@"
    return matrix

#def put_obstacles(x,y,z,c): #block

def cls():
    """Clears terminal"""
    os.system('cls' if os.name=='nt' else 'clear')

def print_matrix(lista):
    for i in lista:
        print(''.join(i))


x_coord, y_coord = 10, 10
#print_matrix(ret_matrix(x_coord, y_coord))

while True:
    list_matrix=ret_matrix(x_coord, y_coord, 30, 30)
    print_matrix(list_matrix)
    char = getch()
    if (char == "a") and (matrix[y_coord][x_coord-1] != "X"):
        x_coord -= 1
    elif (char == "d") and (matrix[y_coord][x_coord+1] != "X"):
        x_coord += 1
    elif (char == "w") and (matrix[y_coord-1][x_coord] != "X"):
        y_coord -= 1
    elif char == "s" and (matrix[y_coord+1][x_coord-1] != "X"):
        y_coord += 1
    else:
        break
