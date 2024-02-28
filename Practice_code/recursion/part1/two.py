def sumNums(num):

    if num != 0:
        return num % 10 + sumNums(num // 10)

    else:
        return 0


print(sumNums(5555))
