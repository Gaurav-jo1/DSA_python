from typing import List

# Maze with Obstacles


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


