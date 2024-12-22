import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Constants
PLAYER_X = "X"  # AI
PLAYER_O = "O"  # Human player
EMPTY = " "      # Empty spot on the board

# Function to print the board with colors
def print_board(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == PLAYER_X:
                print(Fore.RED + " X ", end="|")  # AI move in Red
            elif cell == PLAYER_O:
                print(Fore.BLUE + " O ", end="|")  # Human move in Blue
            else:
                print(Fore.WHITE + "   ", end="|")  # Empty space in White
        print("\n" + "-----" * 3)

# Check for winning state
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

# Check if the board is full (draw)
def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Minimax Algorithm
def minimax(board, depth, is_maximizing_player):
    winner = check_winner(board)
    
    # Terminal conditions
    if winner == PLAYER_X:
        return 1  # AI wins
    if winner == PLAYER_O:
        return -1  # Human wins
    if is_board_full(board):
        return 0  # Draw
    
    # Maximizing for AI (PLAYER_X)
    if is_maximizing_player:
        best = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    
    # Minimizing for Opponent (PLAYER_O)
    else:
        best = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# AI Move (Minimax Decision)
def ai_move(board):
    best_value = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_value = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Function for Human's move
def human_move(board):
    while True:
        try:
            move = int(input(Fore.CYAN + "Enter your move (1-9): ")) - 1
            i, j = divmod(move, 3)
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                break
            else:
                print(Fore.YELLOW + "That spot is taken, try again.")
        except (ValueError, IndexError):
            print(Fore.YELLOW + "Invalid move. Please enter a number between 1 and 9.")

# Function to print win or draw message
def print_result(result):
    if result == PLAYER_X:
        print(Fore.RED + "AI wins!")
    elif result == PLAYER_O:
        print(Fore.BLUE + "You win!")
    else:
        print(Fore.YELLOW + "It's a draw!")

# Play the game
def play_game():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    print_board(board)
    
    while True:
        # Human's turn
        human_move(board)
        print_board(board)
        if check_winner(board):
            print_result(check_winner(board))
            break
        if is_board_full(board):
            print_result(None)
            break
        
        # AI's turn
        print(Fore.GREEN + "AI is making its move...")
        move = ai_move(board)
        board[move[0]][move[1]] = PLAYER_X
        print_board(board)
        
        if check_winner(board):
            print_result(check_winner(board))
            break
        if is_board_full(board):
            print_result(None)
            break

# Start the game
play_game()