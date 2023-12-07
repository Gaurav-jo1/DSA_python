def best_sum(target, numbers):
    array = [None] * (target + 1)

    array[0] = []

    for i in range(target + 1):
        if array[i] is not None:
            for num in numbers:
                index = i + num

                if index <= target:

                    if array[index] is None or len(array[i] + [num]) < len(
                        array[index]
                    ):
                        array[index] = array[i] + [num]

    return array[target]


# Test the function
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
