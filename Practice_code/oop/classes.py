class Directions():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

directions = Directions(5, 4, 3)
print(directions.x)
print(directions.y)
print(directions.z)