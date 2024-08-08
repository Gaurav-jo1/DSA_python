# Can Sum

# Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

# The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

# You may use an element of the array as many times as needed.

# You may assume that all input numbers are nonnegative.


class CanSum:
    def __init__(self) -> None:
        self.memo = {}

    def start(self, target, numbers):
        
        if target == 0:
            return True
        
        if target in self.memo:
            return self.memo[target]

        for num in numbers:
            if num <= target:
                if not self.start(target - num, numbers):
                    self.memo[target - num] = False
                    continue
                else:
                    self.memo[target - num] = True
                    return True
            
        return False


can_sum = CanSum()
# print(can_sum.start(7, numbers=[2, 3]))
# print(can_sum.start(7, numbers=[5, 3, 4, 7]))
# print(can_sum.start(7, numbers=[2, 4]))
# print(can_sum.start(8, numbers=[2, 3, 5]))
print(can_sum.start(300, numbers=[7, 14]))
