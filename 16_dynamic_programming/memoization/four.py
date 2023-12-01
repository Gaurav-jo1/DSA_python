# Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

# The function should return an array containing any combination of elements that add up to exactly the targetSum.
# If there is no combination that adds up to the targetSum, then return null.

# If there are multiple combinations possible, you may return any single one.


class howSum:
    def __init__(self) -> None:
        self.memo = {}

    def how_sum(self, targetSum: int, numbers: list[int]) -> list[int] | None:
        if targetSum in self.memo:
            return self.memo[targetSum]
        if targetSum == 0:
            return []
        if targetSum < 0:
            return None

        for num in numbers:
            if num > targetSum:
                continue

            remainder_result = self.how_sum(targetSum - num, numbers)
            if remainder_result is not None:
                self.memo[targetSum] = remainder_result + [num]
                return self.memo[targetSum]

        self.memo[targetSum] = None
        return None


how_sum = howSum()
# print(how_sum.how_sum(7, [2, 3]))
# print(how_sum.how_sum(7, [5, 3, 4, 7]))
# print(how_sum.how_sum(7, [2, 4]))
print(how_sum.how_sum(8, [2, 3, 5]))
# print(how_sum.how_sum(300, [7, 14]))
