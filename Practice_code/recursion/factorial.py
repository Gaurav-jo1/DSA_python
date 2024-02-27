def factorial(num:int):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError("Input value must be non-negative")
    elif isinstance(num, float):
        raise TypeError("Input must be a int")
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    print(factorial(8))