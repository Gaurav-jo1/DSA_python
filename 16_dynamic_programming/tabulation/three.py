def canSum(targetSum:int, numbers:list[int]) -> str:
    array = [False for _ in range(targetSum + 1)]

    array[0] = True

    for i in range(len(array)):
        if array[i] is True:
            for num in numbers:
                index = i + num
                if index < len(array):
                    array[index] = True

    return array[targetSum]


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [8, 2, 3, 5]))
print(canSum(300, [7, 14]))