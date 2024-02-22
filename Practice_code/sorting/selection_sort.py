def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        min_index = i

        for j in range(i + 1, arr_len):
            if arr[j] <= arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
