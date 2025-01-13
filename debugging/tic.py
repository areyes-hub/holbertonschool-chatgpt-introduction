#!/usr/bin/python3

def print_board(board):
    """Print the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if a player has won the game."""
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        
        # Input handling: Ensure row and column are valid integers
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Check if the row and column are in valid range
                if row not in range(3) or col not in range(3):
                    print("Invalid row or column. Please enter values between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid input! Please enter integers for row and column.")
        
        # Place the move
        board[row][col] = player

        # Switch players
        player = "O" if player == "X" else "X"

    print_board(board)
    # Announce the winner correctly by determining who made the last move
    winner = "O" if player == "X" else "X"
    print(f"Player {winner} wins!")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()

