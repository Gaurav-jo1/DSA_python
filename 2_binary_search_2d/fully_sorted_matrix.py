def main():
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    target = 3

    return search(arr, target)

def search(arr, target):
    for i in range(len(arr)):

        if target > arr[i][-1]:
            continue

        for j in range(len(arr[i])):
            if target == arr[i][j]:
                return print([i, j])

main()