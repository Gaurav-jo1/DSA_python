def say_hello(num:int, step:int= 1):
    if num == 0:
        return
    
    print(f"Hello World {step}")
    say_hello(num= num - 1, step=step + 1)

say_hello(10)