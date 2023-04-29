def main(n):
    for row in range(1, n+ 1):
        for _ in range(1, row + 1):
            print(" * ", end="")
        print()

main(10)