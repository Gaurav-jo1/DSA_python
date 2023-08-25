# Sum of Digits


def SumDigit(n):
    if n > 0:
        last_digit = n % 10
        new_num = (n - last_digit) // 10
        return last_digit + SumDigit(new_num)
    else:
        return 0


print(SumDigit(1582))

# Products of Digites


def ProductDigit(n):
    if n % 10 == n:
        return n
    last_digit = n % 10
    new_num = (n - last_digit) // 10
    return last_digit * ProductDigit(new_num)

print(ProductDigit(12))
