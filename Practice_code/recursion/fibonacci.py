def fibonacci(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num < 0:
        raise ValueError("Input value must be non-negative")
    elif isinstance(num, float):
        raise TypeError("Input value must be Int")
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_series(num: int) -> list[int]:

    if num == 0:
        return []
    elif num == 1:
        return [0]

    answer = [0, 1]

    for i in range(2, num):
        answer.append(fibonacci(i))

    return answer


if __name__ == "__main__":
    print(fibonacci_series(2))
