from colorama import Fore, Back, Style, init

init(autoreset=True)

def draw_colored_board(board):
    for i in range(3):
        row = " | ".join([Back.WHITE + f" {cell} " if cell == " " else Back.RESET + f" {cell} " for cell in board[i]])
        print(row)
        if i < 2:
            print(Fore.BLACK + Back.RESET + "---------")

def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_tie(board):
    return not any(" " in row for row in board)

def ask_move(player):
    try:
        x, y = map(int, input(Fore.CYAN + f"{player}, enter coordinates (1-3 for both x and y): ").strip().split())
        return x, y
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter two integers separated by a space.")
        return ask_move(player)

def make_move(player, board, x, y):
    if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == " ":
        board[x - 1][y - 1] = player
        return True
    else:
        print(Fore.RED + "Invalid move. Please try again with coordinates within 1-3 range.")
        return False

def ask_and_make_move(player, board):
    while True:
        x, y = ask_move(player)
        if make_move(player, board, x, y):
            break

def tic_tac_toe():
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"
        while True:
            draw_colored_board(board)
            ask_and_make_move(player, board)
            if check_win(player, board):
                print(Fore.GREEN + f"{player} wins!")
                break
            if check_tie(board):
                print(Fore.YELLOW + "It's a tie!")
                break
            player = "O" if player == "X" else "X"
        restart = input(Fore.MAGENTA + "Do you want to play again? (y/n) ")
        if restart.lower() != "y":
            break

tic_tac_toe()
