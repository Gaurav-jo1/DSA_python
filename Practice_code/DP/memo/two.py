class gridTravel():
    
    def __init__(self) -> None:
        self.memo = {}
        
    def start(self, rows, cols):
        if rows == 0 or cols == 0:
            return 0
        
        if rows == 1 and cols == 1:
            return 1
        
        key = f"{cols},{rows}"
        
        if key in self.memo:
            return self.memo[key]
        
        self.memo[key] = self.start(rows- 1, cols) + self.start(rows, cols - 1)

        return self.memo[key]

travel = gridTravel()
print(travel.start(2, 3))
print(travel.start(3, 2))
print(travel.start(3, 3))
print(travel.start(50, 50))
