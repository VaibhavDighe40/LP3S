def is_safe(board, row, col, n):
    # Check if a queen can be placed at the given position
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    # Recursive function to solve N-Queens problem using backtracking
    if row == n:
        # All queens are placed successfully, print the solution
        print_board(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place queen and move to the next row
            board[row][col] = 1
            res = solve_n_queens_util(board, row + 1, n) or res
            # Backtrack if placing a queen doesn't lead to a solution
            board[row][col] = 0

    return res

def solve_n_queens():
    # Get the size of the chessboard from user input
    n = int(input("Enter the size of the chessboard (N): "))
    board = [[0] * n for _ in range(n)]

    # Solve and print solutions
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
    else:
        print("All solutions printed successfully.")

def print_board(board):
    # Helper function to print the chessboard
    for row in board:
        print(" ".join(map(str, row)))
    print()

# Example: Solve the N-Queens problem based on user input
solve_n_queens()
