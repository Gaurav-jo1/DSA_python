# Q- Finding the starting and ending index of the target

nums = [5, 7, 7, 7, 7, 8, 8, 10]
target = 7


def positionA():
    ans = [-1, -1]

    ans[0] = positionE(True)
    ans[1] = positionE(False)

    return ans


def positionE(findStartIndex):
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


print(positionA())


