people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person:person["name"])

print(people)

# Using Lambda
# x = lambda a: a + 20
# print(x(10))

# Using Function
# def add(b):
#     adding = b + 10
#     return adding

# print(add(10))    