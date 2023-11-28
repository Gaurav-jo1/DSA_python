# Calculate the 40th number of the fiboncci sequence.

# count the number of different ways to move through a grid of 6 x 9 grid.

# Given a set of coins, how can we make 27 cents in the least number of coins?

# Given a set of substrings, what are the possible ways to construct the string "potentpot"?

# Write a function 'fib(n)' that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence.

# fib(n) - 1, 1 , 2, 3, 5, 8, 13, 21, 34, ...


class Fib:
    def find_value(
        self, num: int, prev_value: int = 0, current_value: int = 1, count: int = 1
    ):
        temp_current = current_value
        current_value += prev_value
        prev_value = temp_current
        count += 1

        if count == num:
            return current_value

        return self.find_value(num, prev_value, current_value, count)


class Fib:
    def fib_value(self, num: int):
        if num <= 2:
            return 1

        return self.fib_value(num - 1) + self.fib_value(num - 2)


series = Fib()
print(series.fib_value(10))
