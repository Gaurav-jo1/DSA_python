# gridTraveler tabulation


def gridTraveler(r, c):
    array = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    array[1][1] = 1

    for row in range(r + 1):
        for column in range(c + 1):
            if column < c:
                array[row][column + 1] += array[row][column]

            if row < r:
                array[row + 1][column] += array[row][column]

    return array[r][c]


print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(3, 3))
print(gridTraveler(18, 18))