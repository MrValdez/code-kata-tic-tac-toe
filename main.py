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



reset()
display_board()