from typing import List

def Maze(row: int, column: int):
    if row == 1 or column == 1:
        return 1

    left = Maze(row - 1, column)
    right = Maze(row, column - 1)

    return left + right


# print(Maze(3, 3))

def MazeStep(row: int, column: int, step: str = "") -> List[str]:
    paths = []

    # Base case: we reached the end of the maze
    if row == 1 and column == 1:
        return [step]

    
    # Check if we can move down (row > 1)
    if row > 1:
        paths += MazeStep(row - 1, column, step=step + "D")
    # Check if we can move right (column > 1)
    if column > 1:
        paths += MazeStep(row, column - 1, step=step + "R")

    return paths

# print(MazeStep(3, 3))

def MazeStepDigonal(row: int, column: int, step: str = "") -> List[str]:
    paths = []

    # Base case: we reached the end of the maze
    if row == 1 and column == 1:
        return [step]

    
    # Check if we can move down (row > 1)
    if row > 1:
        paths += MazeStepDigonal(row - 1, column, step=step + "D")
    # Check if we can move right (column > 1)
    if column > 1:
        paths += MazeStepDigonal(row, column - 1, step=step + "R")
    
    if column > 1 and row > 1:
        paths += MazeStepDigonal(row -1, column -1, step=step + "O")

    return paths

print(MazeStepDigonal(3, 3))