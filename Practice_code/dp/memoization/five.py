# Best Some

# Write a function `bestSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
# The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
# If there is a tie for the shortest combination, you may return any one of the shortest.
from typing import List


class bestSum:
    def __init__(self) -> None:
        self.memo = {}

    def start(self, targetSum: int, numbers: List[int]):

        if targetSum in self.memo:
            return self.memo[targetSum]

        if targetSum == 0:
            return []

        if targetSum < 0:
            return None

        shortestCombination = None

        for number in numbers:
            if number > targetSum:
                continue

            remainder = targetSum - number
            remainderCombination = self.start(remainder, numbers)

            if remainderCombination is not None:
                combination = [number] + remainderCombination

                if shortestCombination is None or len(shortestCombination) > len(
                    combination
                ):
                    shortestCombination = combination

        self.memo[targetSum] = shortestCombination

        return shortestCombination


best_sum = bestSum()

# print(best_sum.start(7, [2, 3]))
# print(best_sum.start(7, [5, 3, 4, 7]))
# print(best_sum.start(8, [2, 3, 5]))
# print(best_sum.start(8, [1, 4, 5]))
print(best_sum.start(100, [1, 2, 5, 25]))
