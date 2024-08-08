def combinationSum(nums, target):
    result = []
    nums_len = len(nums)
    

    def comb(nums, index=0):
        nonlocal result, nums_len

        if not index < nums_len:
            return []

        if sum(nums) == target:
            result.append(nums)

        comb(nums[1:], index + 1)
        comb(nums, index + 1)

        return

    comb(nums)

    return result

nums = [2, 5, 6, 9]
target = 9

print(combinationSum(nums, target))