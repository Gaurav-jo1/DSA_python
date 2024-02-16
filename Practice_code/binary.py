def b_search(arr, target):

    if not arr or target is None:
        return -1

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid_index = start + (end - start) // 2
        mid_value = arr[mid_index]

        if target == mid_value:
            return mid_index

        elif target > mid_value:
            start = mid_index + 1

        else:
            end = mid_index - 1

    return -1


def ceiling(arr, target):

    if not arr or target is None or target > arr[-1]:
        return None

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid_index = start + (end - start) // 2
        mid_value = arr[mid_index]

        if target == mid_value:
            return mid_value

        elif target > mid_value:
            start = mid_index + 1
        else:
            end = mid_index - 1

    return arr[start]

def floor(arr, target):
    if not arr or target is None or target < arr[1]:
        return None

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid_index = start + (end - start) // 2
        mid_value = arr[mid_index]

        if target == mid_value:
            return mid_value

        elif target > mid_value:
            start = mid_index + 1
        else:
            end = mid_index - 1

    return arr[end]