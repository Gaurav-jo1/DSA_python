def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if it's safe to place a queen at board[row][col]
        # Check the row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check the upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check the lower-left diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col):
        # If all queens are placed successfully, we have found a solution
        if col >= n:
            solutions.append([row[:] for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                # Place a queen at board[i][col]
                board[i][col] = 1
                # Recur to place queens in the next columns
                solve(board, col + 1)
                # Backtrack and remove the queen to explore other possibilities
                board[i][col] = 0

    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions

# Example usage:
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
    print()
