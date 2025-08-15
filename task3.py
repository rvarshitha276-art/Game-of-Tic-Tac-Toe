import random

# Display the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if someone has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(spot == player for spot in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(spot != " " for row in board for spot in row)

# Player move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Spot already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number between 1 and 9.")

# Computer move (random choice)
def computer_move(board):
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_spots:
        row, col = random.choice(empty_spots)
        board[row][col] = "O"

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X'.")
    print("Board positions:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9\n")

    while True:
        print_board(board)
        player_move(board)
        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        computer_move(board)
        if check_winner(board, "O"):
            print_board(board)
            print("💻 Computer wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Run the game
tic_tac_toe()
