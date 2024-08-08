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

        for num in numbers:

            if num < 0:
                continue

            remainder_sum = self.best_sum(targetSum - num, numbers)

            if remainder_sum is not None:
                new_combo = remainder_sum + [num]

                if targetSum in self.memo and len(self.memo[targetSum]) < len(
                    new_combo
                ):
                    continue
                else:
                    self.memo[targetSum] = new_combo

        if targetSum in self.memo:
            return self.memo[targetSum]
        else:
            return None


best_sum = bestSum()
# print(best_sum.best_sum(7, [2, 3]))
# print(best_sum.best_sum(7, [5, 3, 4, 7]))
# print(best_sum.best_sum(8, [2, 3, 5]))
# print(best_sum.best_sum(8, [1, 4, 5]))
print(best_sum.best_sum(100, [1, 2, 5, 25]))
