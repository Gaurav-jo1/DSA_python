# Opening a file
file = open('./hello.txt', 'w')  # opens the file in write mode

# Writing to a file
file.write('Hello, this is some content to write to the file.')

# Appending to a file
file = open('./hello.txt', 'a')  # opens the file in append mode
file.write('\nThis is additional content appended to the file.')

# Closing a file
file.close()

# Reading from a file
# with open('./hello.txt', 'r') as file:
#     content = file.read()
#     print(content)


reading = open('./hello.txt', 'r')

content = reading.read()
print(content)