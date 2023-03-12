# Q- Finding the starting and ending index of the target

# nums = [5, 7, 7, 7, 7, 8, 8, 10]
# target = 7


# def positionA():
#     ans = [-1, -1]

#     ans[0] = positionE(True)
#     ans[1] = positionE(False)

#     return ans


# def positionE(findStartIndex):
#     start = 0
#     end = len(nums) - 1
#     ans = -1
#     while start <= end:
#         mid = (start + end) // 2
#         if target < nums[mid]:
#             end = mid - 1
#         elif target > nums[mid]:
#             start = mid + 1
#         else:
#             ans = mid
#             if (findStartIndex):
#                 end = mid - 1
#             else:
#                 start = mid + 1
#     return ans


# print(positionA())

# _____________________________________________________________

# Q- Finding the target on a Infinite array

# def main():
#     arr = [3,5,7,9,10,90,100,130,140,160,170]
#     target = 200

#     return indexS(arr, target)

# def indexS(arr, target):
#     start = 0
#     end = 1

#     while target > arr[end]:
#         newStart = end + 1
#         end = end + (end - start + 1) * 2
#         start = newStart

#     return searchIndex(arr,target,start,end)

# def searchIndex(arr,target,start,end):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == arr[mid]:
#             return mid
#         elif target < arr[mid]:
#             end = mid - 1
#         elif target > arr[mid]:
#             start = mid + 1

# print(main())

# _____________________________________________________________

# Q- Peak index in mountain array 
# Q- Find peak and then search in a mountain array

# Mountain array is increading first and decresing after

# arr = [24,69,100,99,79,78,67,36,26,19]
# arr = [0, 1, 3, 4, 6, 9, 5, 3, 2]
# arr = [0,10,5,2]
# arr = [0,1,0]
# arr = [0,2,1,0]
# arr = [3,5,3,2,0]
# arr = [40,48,61,75,100,99,98,39,30,10]
# arr = [3,4,11,15,18,24,30,36,44,57,62,64,68,88,90,91,99,100,81,74,61,55,49,39,23,15,11]


# def main():
#     # arr = [0, 1, 3, 4, 6, 9, 5, 3, 2]
#     arr = [0,10,5,2]
#     # arr = [40,48,61,75,100,99,98,61,39,30,10]
#     target = 2

#     high = highN(arr)

#     firstHalf = findT(arr, target, 0, high, True)
#     # print("firstHalf", firstHalf)

#     if firstHalf != -1 :
#         return firstHalf
#     else:
#         return findT(arr, target, high, len(arr) - 1, False)


# def highN(arr):
#     start = 0
#     end = len(arr) - 1
#     while start <= end:
#         highest = (start + end) // 2
#         if arr[highest - 1] < arr[highest] > arr[highest + 1]:
#             return highest
#         elif arr[highest] > arr[highest - 1]:
#             start = highest
#         elif arr[highest] < arr[highest - 1]:
#             end = highest


# def findT(arr, target, start, end, searchingLeft):
#     starting = start
#     ending = end

#     if searchingLeft:
#         while starting <= ending:
#             mid = (starting + ending) // 2
#             if arr[mid] == target:
#                 return mid
#             elif target > arr[mid]  :
#                 starting = mid + 1
#             elif target < arr[mid]:
#                 ending = mid - 1 
#         return - 1
#     else:
#         while starting <= ending:
#             mid = (starting + ending) // 2
#             if arr[mid] == target:
#                 return mid
#             elif target < arr[mid]  :
#                 starting = mid + 1
#             elif target > arr[mid]:
#                 ending = mid - 1 
#         return - 1



# print(main())

# _____________________________________________________________

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