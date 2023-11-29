class gridTravel:
    def __init__(self) -> None:
        self.memo = {}

    def start(self, column: int, row: int):
        if column == 1 and row == 1:
            return 1

        if column == 0 or row == 0:
            return 0

        key = f"{column},{row}"

        if key in self.memo:
            return self.memo[key]

        self.memo[key] = self.start(column, row - 1) + self.start(column - 1, row)

        return self.memo[key]


travel = gridTravel()
print(travel.start(1, 1))
print(travel.start(2, 3))
print(travel.start(3, 2))
print(travel.start(3, 3))
print(travel.start(50, 50))
