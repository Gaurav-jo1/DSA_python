def binary_search_2d(array, target):

    row = 0
    col = len(array[row]) - 1

    while row <= (len(array) - 1) and col >= 0:

        curr_val = array[row][col]

        if target == curr_val:
            return (row, col)

        elif target > curr_val:
            row += 1

        else:
            col -= 1

    return (-1, -1)


print(binary_search_2d(array=[[1, 3, 5], [7, 9, 11], [13, 15, 17]], target=9))
