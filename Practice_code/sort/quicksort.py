def quickSort(arr):

    if len(arr) <= 1:
        return arr

    pivot = len(arr) // 2

    left_arr = [x for x in arr if x < arr[pivot]]
    mid_arr = [x for x in arr if x == arr[pivot]]
    right_arr = [x for x in arr if x > arr[pivot]]
    
    return quickSort(left_arr) + mid_arr + quickSort(right_arr)

print(quickSort([3, 6, 8, 10, 1, 2, 1]))