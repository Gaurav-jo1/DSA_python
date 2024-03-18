file = open('./hello.txt', 'w')
file.write("Hello this is Gaurav Joshi.")

file = open('./hello.txt', 'a')  # opens the file in append mode
file.write('\nThis is additional content appended to the file.')

file.close()

content = open('./hello.txt', 'r')
content = content.read()
print(content)