def sort(arr):
    for i in range(1, len(arr)):
        while arr[i-1] > arr[i] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1

print(sort([34, 42, 22, 54, 19, 5]))
