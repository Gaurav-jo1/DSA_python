
# Search in Rotated sorted array

def main():
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    # arr = [3,4,5,6,7,0,1,2]
    target = 6

    high = highN(arr)

    firstHalf = findT(arr, target, 0, high)

    if firstHalf != -1:
        return firstHalf
    else:
        return findT(arr, target, high + 1, len(arr) - 1)

def highN(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[start] > arr[mid]:
            end = mid
        elif arr[start] < arr[mid]:
            start = mid
        else:
            return mid

def findT(arr, target, start, end):
    starting = start
    ending = end

    while starting <= ending:
        mid = (starting + ending) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]  :
            starting = mid + 1
        elif target < arr[mid]:
            ending = mid - 1
    return - 1

print(main())


# Q- Searching in rotaed array including duplicate element

# _____________________________________________________________

# Q - Find the number of rotation count in rotated sorted array

# Ans - Find the pivot (highest number in a sorted arry) and plus 1, that is going to be the number of rotations

# _____________________________________________________________