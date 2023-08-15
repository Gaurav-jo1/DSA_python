
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)
