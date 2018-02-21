board = None
is_playing = True

def reset():
    global board, is_playing
    board = [" "] * 9
    is_playing = True

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
symbol_p2 = "O"

# we calculate the maximum number of turns between players
max_turns = round((9 / 2) + .5)
symbol_sequence = [symbol_p1, symbol_p2] * max_turns

while is_playing:
    symbol = symbol_sequence.pop()
    x, y = ask_for_move(symbol)
    play_move(symbol, x, y)
    display_board()