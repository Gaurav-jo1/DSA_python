def cycle_sort(arr):
    n = len(arr)

    for cycle_start in range(n - 1):
        item = arr[cycle_start]

        # Find the position where we put the element
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        # If the element is already in the correct position, continue to the next cycle
        if pos == cycle_start:
            continue

        # Otherwise, put the element to the correct position and rotate the cycle
        while item == arr[pos]:
            pos += 1

        arr[pos], item = item, arr[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]

# Example usage:
my_list = [5, 2, 1, 7, 4, 6, 3]
cycle_sort(my_list)
print("Sorted list:", my_list)
