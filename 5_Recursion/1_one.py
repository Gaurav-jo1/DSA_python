def fibonacci(n):
    if n < 2:
        return n
    else:
        answer = fibonacci(n - 1) + fibonacci(n - 2)
        return answer

# print(fibonacci(n=12))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6)) 