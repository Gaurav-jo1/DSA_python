# Q- Position of an element in Infinite Sorted array
def binary_search(arr, target):
    left, right = 0, 1
    while arr[right] < target:
        left = right
        right *= 2
    print("left:", left)  # left: 8
    print("right:", right)  # right: 16
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([3, 5, 7, 9, 10, 90, 100, 130, 140, 160 , 170], 10))