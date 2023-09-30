# Maze with Obstacles

from typing import List

def MazeStepRestriction(row: int, column: int, step: str = "") -> List[str]:
    paths = []

    # Base case: we reached the end of the maze
    if row == 1 and column == 1:
        return [step]
    
    if row == 2 and column == 2:
        return []
    
    # Check if we can move down (row > 1)
    if row > 1:
        paths += MazeStepRestriction(row - 1, column, step=step + "D")
    # Check if we can move right (column > 1)
    if column > 1:
        paths += MazeStepRestriction(row, column - 1, step=step + "R")

    return paths

print(MazeStepRestriction(3, 3))

def MazeStepAll(down: int, right: int, step: str = "") -> List[str]:
    paths = []

    # Base case: we reached the end of the maze
    if down == 1 and right == 1:
        return [step]
    
    # Check if we can move down (row > 1)
    if down > 1:
        paths += MazeStepAll(down - 1, right, step=step + "D")
    # Check if we can move right (column > 1)
    if right > 1:
        paths += MazeStepAll(down, right - 1, step=step + "R")

    return paths

print(MazeStepAll(3, 3))