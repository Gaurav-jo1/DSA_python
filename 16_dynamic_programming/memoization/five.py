# Best Some

# Write a function `bestSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
# The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
# If there is a tie for the shortest combination, you may return any one of the shortest.


class bestSum:
    def __init__(self) -> None:
        self.memo = {}

    def best_sum(self, targetSum, numbers):
        if targetSum in self.memo:
            return self.memo[targetSum]
        if targetSum == 0:
            return []

        if targetSum < 0:
            return None

        shortestCombination = None

        for num in numbers:
            if num > targetSum:
                continue

            remainder = targetSum - num
            remainderCombination = self.best_sum(remainder, numbers)

            if remainderCombination is not None:
                combination = remainderCombination + [num]

                if shortestCombination is None or len(combination) < len(
                    shortestCombination
                ):
                    shortestCombination = combination

        self.memo[targetSum] = shortestCombination

        return shortestCombination


best_sum = bestSum()
# print(best_sum.how_sum(7, [2, 3]))
# best_sum.best_sum(7, [5, 3, 4, 7])
# print(best_sum.best_sum(8, [2, 3, 5]))
# print(best_sum.best_sum(8, [1, 4, 5]))
print(best_sum.best_sum(100, [1, 2, 5, 25]))
