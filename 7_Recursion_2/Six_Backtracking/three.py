# You are making some changes while going below to the recursion call,
# So when you go outside those recursion call's the changes were made via those recursion call
# Should also not be avaiable.


def allPath(p, maze, r, c):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        print(p)
        return

    if not maze[r][c]:
        return

    # Consider this block in the path
    maze[r][c] = False

    if r < len(maze) - 1:
        allPath(p + "D", maze, r + 1, c)

    if c < len(maze[0]) - 1:
        allPath(p + "R", maze, r, c + 1)

    if r > 0:
        allPath(p + "U", maze, r - 1, c)

    if c > 0:
        allPath(p + "L", maze, r, c - 1)

    # Restore the original value before exiting the function
    maze[r][c] = True


# Example usage:
maze = [
    [True, True, False, True],
    [True, False, True, True],
    [True, True, True, True],
    [False, True, True, True],
]

allPath("", maze, 0, 0)
