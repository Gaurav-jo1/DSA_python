# Calculate the 40th number of the fiboncci sequence.

# Write a function 'fib(n)' that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence.


class FibFirst:
    def fib_value(self, num: int):

        if num == 0:
            return 0

        if num == 1:
            return 1

        return self.fib_value(num - 1) + self.fib_value(num - 2)


# series_1 = FibFirst()
# print(series_1.fib_value(10))


class FibSecond:
    def fib_value(
        self, num: int, prev_value: int = 0, cur_val: int = 1, count: int = 1
    ):

        if num == count:
            return cur_val

        new_val = cur_val + prev_value
        prev_value = cur_val
        cur_val = new_val

        return self.fib_value(num, prev_value, cur_val, count + 1)


series_2 = FibSecond()
print(series_2.fib_value(50))


class FibThird:
    def fib_value(self, num:int, memo={}):
        if num in memo:
            return memo[num]
        
        if num == 0:
            return 0
        
        elif num == 1:
            return 1
        
        memo[num] = self.fib_value(num - 1) + self.fib_value(num - 2)

        return memo[num]
        
series_3 = FibSecond()
print(series_3.fib_value(50))