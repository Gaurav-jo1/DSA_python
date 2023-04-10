# Q - Peak Index in a Mountain Array
# LeetCode - https://leetcode.com/problems/peak-index-in-a-mountain-array/

def binary_search(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] > arr[mid - 1]:
            start = mid 
        else:
            end = mid
     

# print(binary_search([2, 4, 5, 6, 7, 9, 11, 13, 6, 3, 2, 1]))
print(binary_search([0,10,5,2]))