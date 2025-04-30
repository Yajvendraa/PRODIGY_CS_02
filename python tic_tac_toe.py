import random

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def check_winner(brd, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
    for cond in win_conditions:
        if brd[cond[0]] == brd[cond[1]] == brd[cond[2]] == player:
            return True
    return False

def is_full(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i in range(9) if brd[i] == ' ']

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1,10) and board[int(move)-1] == ' ':
            board[int(move)-1] = 'X'
            break
        else:
            print("Invalid move. Try again.")

def ai_move():
    # Try to win
    for move in get_available_moves(board):
        copy = board[:]
        copy[move] = 'O'
        if check_winner(copy, 'O'):
            board[move] = 'O'
            return

    # Try to block player from winning
    for move in get_available_moves(board):
        copy = board[:]
        copy[move] = 'X'
        if check_winner(copy, 'X'):
            board[move] = 'O'
            return

    # Else, pick random
    move = random.choice(get_available_moves(board))
    board[move] = 'O'

def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and AI is 'O'")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        ai_move()
        print("AI's move:")
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

play_game()
