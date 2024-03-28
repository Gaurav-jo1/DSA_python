# Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

# The function should return an array containing any combination of elements that add up to exactly the targetSum.
# If there is no combination that adds up to the targetSum, then return null.

# If there are multiple combinations possible, you may return any single one.
from typing import List


class howSum:
    def __init__(self) -> None:
        self.memo = {}

    def how_sum(self, targetSum: int, array: List[int]):
        if targetSum in self.memo:
            return self.memo[targetSum]

        if targetSum == 0:
            return []

        if targetSum < 0:
            return None

        for number in array:
            if number > targetSum:
                continue

            child = self.how_sum(targetSum - number, array)

            if child is not None:
                self.memo[targetSum] = [number] + child
                return self.memo[targetSum]

        self.memo[targetSum] = None
        return self.memo[targetSum]


how_sum = howSum()
# print(how_sum.how_sum(7, [2, 3]))
# print(how_sum.how_sum(7, [5, 3, 4, 7]))
# print(how_sum.how_sum(7, [2, 4]))
print(how_sum.how_sum(8, [2, 3, 5]))
# print(how_sum.how_sum(300, [7, 14]))
