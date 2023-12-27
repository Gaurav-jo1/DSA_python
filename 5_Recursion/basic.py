def helloWorld(n, step=1):
    num = n
    if 1 <= num:
        print(f"Hello World {step}")
        step += 1
        helloWorld(n - 1, step)

helloWorld(10)
