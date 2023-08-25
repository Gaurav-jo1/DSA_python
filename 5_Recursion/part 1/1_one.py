# Printing the Number in reverse and non-reverse order

def numBoth(n):
    if n == 0:
        return

    print(n)

    numBoth(n - 1)

    if n != 1:
        print(n)

numBoth(5)
