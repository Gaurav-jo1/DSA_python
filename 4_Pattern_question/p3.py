def main(n):
    num = n
    for _ in range(1, n+1):
        for _ in range(num):
            print(" * ", end="")
        num -= 1
        print()

main(8)