def pattern(n=4):
    if n < 1:
        return

    print("* " * n)

    pattern(n - 1)


# pattern()


def pattern2(row=4, column=4):
    if row == 0:
        return

    print("* " * column)

    pattern2(row - 1, column - 1)


# pattern2()


def pattern3(row=4, column=1):
    if row == 0:
        return

    print("*" * column)

    pattern3(row=row - 1, column=column + 1)


pattern3()
