def RowColMatrix():
    arr = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [28, 29, 37, 49],
        [33, 34, 38, 50]
    ]

    target = 33

    return search(arr, target)

def search(arr, target):
    r = 0
    c = len(arr) - 1

    while r < len(arr) and c >= 0:
        if arr[r][c] == target:
            return r, c
        elif arr[r][c] < target:
            r = r + 1
        else:
            c = c - 1
    return [-1, -1]


print(RowColMatrix())
