def searchRange(nums, target):
    ans = [-1, -1]

    start = positionE(True, nums, target)
    end = positionE(False, nums, target)

    ans[0] = start
    ans[1] = end

    return ans


def positionE(findStartIndex, nums, target):
    start = 0
    end = len(nums) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            ans = mid
            if (findStartIndex):
                end = mid - 1
            else:
                start = mid + 1
    return ans


print(searchRange([5, 7, 7, 8, 8, 10], 8))
