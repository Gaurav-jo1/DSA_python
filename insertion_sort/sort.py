def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                arr[j + 1] = arr[j]
                position = j
            else:
                break
        arr[position] = current_value
    return arr

print(insertion_sort([5, 4,  3, 2, 1]))