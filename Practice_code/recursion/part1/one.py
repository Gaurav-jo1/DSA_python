def numBoth(num):
    if num >= 1:
        print(num)
        numBoth(num - 1)

    if num > 1:
        print(num)

numBoth(5)
