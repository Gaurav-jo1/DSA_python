arr = [2, 4, 5, 6, 7, 12, 14, 15, 17, 19, 21, 24]

target = 21

def sorting():
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Ceiling = Number which is > of = the target element
# Here, if target = 16
# Then the ceiling of the number is 17

def ceiling():
    start = 0
    end = len(arr) - 1
    while start <= end:
        pass
    
    return arr[start]

# Floor - Greatest number smaller to the target number
# Here, If target = 16
# Then the floor of the number is 15

def floor():
    start = 0
    end = len(arr) - 1
    while start <= end:
        pass
    
    return arr[end]

print(sorting())

# Leetcode question to checkout

# 1. https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# 2. https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/