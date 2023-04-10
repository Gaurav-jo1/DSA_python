# Split Array Largest Sum
# Leetcode link - https://leetcode.com/problems/split-array-largest-sum

def splitArray(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        count = 1
        total = 0

        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1

        if count > k:
            left = mid + 1
        else:
            right = mid

    return left

print(splitArray([7, 2, 5, 10, 8], 2))
