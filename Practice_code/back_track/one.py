import sys
from typing import List


def Maze(rows: int, cols: int) -> List[str]:
    if rows == 1 and cols == 1:
        return 1

    down, right = 0, 0

    if rows >= 1:
        down = Maze(rows - 1, cols)

    if cols >= 1:
        right = Maze(rows, cols - 1)

    return down + right


# maze = Maze(3, 3)
# sys.stdout.write(str(maze) + "\n")
# sys.stdout.flush()


def MazeStep(rows:int, cols:int, steps="") -> List[str]:
    if rows == 1 and cols == 1:
        return [steps]
    
    down, right = [], []
    
    if rows >= 1:
        down = MazeStep(rows - 1, cols, steps + "D")

    if cols >= 1:
        right = MazeStep(rows, cols - 1, steps + "R")

    return down + right

# maze = MazeStep(3, 3)
# sys.stdout.write(str(maze) + "\n")
# sys.stdout.flush()

def MazeStepHori(rows:int, cols:int, steps="") -> List[str]:
    if rows == 1 and cols == 1:
        return [steps]
    
    down, right, horiz = [], [], []
    
    if rows >= 1:
        down = MazeStepHori(rows - 1, cols, steps + "D")

    if cols >= 1:
        right = MazeStepHori(rows, cols - 1, steps + "R")

    if rows >= 1 and cols >= 1:
        horiz = MazeStepHori(rows - 1, cols - 1, steps + "H")

    return down + right + horiz

maze = MazeStepHori(3, 3)
sys.stdout.write(str(maze) + "\n")
sys.stdout.flush()
