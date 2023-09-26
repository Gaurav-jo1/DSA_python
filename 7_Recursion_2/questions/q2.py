def main():
    dice("", 4)

def dice(p, target):
    if target == 0:
        print(p)
        return

    for i in range(1, 7):
        if i <= target:
            dice(p + str(i), target - i)

if __name__ == "__main__":
    main()
