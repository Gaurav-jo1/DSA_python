def announce(func):
    def wrapper(*args):
        print("Hey there function is starting.")
        result = func(*args)
        print("Goodbye.")
        return result
    return wrapper

@announce
def hello(name: str):
    print(f"Hello {name}, welcome here.")

hello("Gaurav")
