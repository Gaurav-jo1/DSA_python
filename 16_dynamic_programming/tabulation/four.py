def howSum(target, number):
    array = [None for _ in range(target + 1)]
    array[0] = []

    arr_length = len(array)
    for i in range(arr_length):
        if array[i] is not None:
            for num in number:
                index = num + i
                if index < arr_length:
                    array[index] = array[i] + [num]

    return array[target]


print(howSum(7, [2, 3]))
print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [2, 4]))
print(howSum(8, [2, 3, 5]))
print(howSum(300, [7, 14]))
