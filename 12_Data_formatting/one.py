def string_join():
    string_array = []

    string_array.append("H")
    string_array.append("e")
    string_array.append("l")
    string_array.append("l")
    string_array.append("o")

    print(string_array)

    result_string = ", ".join(string_array)

    print(result_string)

def string_joining():
    name = "John"
    age = 30

    format_string = "My name is {}, I am {}".format(name, age)

    print(format_string)


def string_methods():
    # Define a string
    string = "  Hello, welcome to the world of Python  "

    # Convert to upper and lower case
    print(string.upper())  # Output:   HELLO, WELCOME TO THE WORLD OF PYTHON
    print(string.lower())  # Output:   hello, welcome to the world of python

    # Remove leading and trailing whitespaces
    print(string.strip())  # Output: Hello, welcome to the world of Python

    # Split the string
    print(string.split(","))  # Output: ['  Hello', ' welcome to the world of Python  ']

    # Replace substrings
    new_string = string.replace("Python", "Java")
    print(new_string)  # Output:   Hello, welcome to the world of Java

    # Find the index of a substring
    print(string.find("welcome"))  # Output: 8

    # Check if the string starts or ends with a specific substring
    print(string.startswith("Hello"))  # Output: False
    print(string.endswith("Python"))  # Output: True


if __name__ == "__main__":
    # string_join()
    string_joining()
    # string_methods()
