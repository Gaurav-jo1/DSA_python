def main():
    n = 4
    board = [[False for _ in range(n)] for _ in range(n)]  # Initialize the chessboard with all empty squares

    print(queens(board, row=0))  # Start the NQueens solver with an empty board at the first row

def queens(board, row):
    if row == len(board):
        display(board)  # If all queens are placed (base case), display the board
        print()
        return 1  # Return 1 to indicate a valid placement of queens

    count = 0  # Initialize a count to keep track of valid solutions

    for col in range(len(board)):
        if is_safe(board, row, col):  # Check if it's safe to place a queen at this position
            board[row][col] = True  # Place the queen
            count += queens(board, row + 1)  # Recursively try to place queens in the next row
            board[row][col] = False  # Backtrack by removing the queen

    return count  # Return the count of valid solutions

def is_safe(board, row, col):
    # Check if there is no queen in the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check if there is no queen on the left diagonal
    max_left = min(row, col)
    for i in range(1, max_left + 1):
        if board[row - i][col - i]:
            return False

    # Check if there is no queen on the right diagonal
    max_right = min(row, len(board) - col - 1)
    for i in range(1, max_right + 1):
        if board[row - i][col + i]:
            return False

    return True  # It's safe to place a queen at this position

def display(board):
    for row in board:
        for element in row:
            if element:
                print("Q ", end="")  # Print 'Q' for a queen
            else:
                print(". ", end="")  # Print '.' for an empty square
        print()

if __name__ == "__main__":
    main()
