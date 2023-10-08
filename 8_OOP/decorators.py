# Function that takes a function as input
# and return a modified version of that function

def announce(hello):
    def wrapper():
        print("About to run the function...")
        hello()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, World! by a")

hello()