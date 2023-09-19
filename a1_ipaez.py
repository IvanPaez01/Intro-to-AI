import random

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(i, end=" ")
        for cell in row:
            print(cell, end=" ")
        print()

def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False

def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")

def computer_move(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

def main():
    print("Welcome to the Tic-Tac-Toe game!")
    while True:
        board = initialize_board()
        display_board(board)

        while True:
            player_move(board)
            if check_winner(board, "X"):
                display_board(board)
                print("Congratulations! You won!")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            computer_move(board)
            if check_winner(board, "O"):
                display_board(board)
                print("Computer won! Try again.")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            display_board(board)

        if input("Do you want to play another round? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()
def minmax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minmax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minmax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval


def computer_move(board):
    best_score = -float('inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minmax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        board[best_move[0]][best_move[1]] = "O"
