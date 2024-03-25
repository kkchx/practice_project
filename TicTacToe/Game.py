def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("----------")


def ask_move(player):
    try:
        x, y = map(int, input(f"{player}, enter coordinates (1-3 for both x and y): ").strip().split())
        return x, y
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
        return ask_move(player)


def make_move(player, board, x, y):
    if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == " ":
        board[x - 1][y - 1] = player
        return True
    else:
        print("Invalid move. Please try again with coordinates within 1-3 range.")
        return False


board = [[" " for i in range(3)] for j in range(3)]
player = "x"
draw_board(board)
x, y = ask_move(player)
make_move(player,board,x,y)