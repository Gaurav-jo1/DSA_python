def main(n):
    num = n
    for i in range(1, n+1):
        for _ in range(1, i+1):
            print(" *", end="")
        print()
    for _ in range(1, n):
        for _ in range(1, num):
            print(" *", end="")
        num -= 1
        print()

main(5)