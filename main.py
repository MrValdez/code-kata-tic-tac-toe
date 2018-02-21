board = None

def reset():
    global board
    board = [0] * 9

def display_board():
    for rows in [board[:3], board[3:6], board[6:]]:
        print("|", end="")
        for cell in rows:
            print(cell,end="|")
        print("")

def ask_for_move(symbol):
    coordinates = input("""Where do you want to put {} (use "x, y" format)? """.format(symbol))

    try:
        coordinates = coordinates.split(",")
        x, y = coordinates
        x = int(x.strip())
        y = int(y.strip())
        
        if 3 > x <= 0:
            raise ValueError

    except ValueError:
        print(""" Invalid input.
 Please use "x, y" format. Top-left coordinate is 1, 1
 Example: 2, 2
""")
        return ask_for_move(symbol)

    return x, y

def play_move(symbol, x, y):
    # move coordinates to zero start
    x -= 1
    y -= 1
    board[(y * 3) + x] = symbol

reset()
display_board()

symbol_p1 = "X"
x, y = ask_for_move(symbol_p1)
play_move(symbol_p1, x, y)
display_board()