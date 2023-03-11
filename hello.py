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