# Write a Program to check if the seats are avilable for passangers
import os 

class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passangers = []

    def add_passangers(self,name):
        
        if self.seats_left():
            self.passangers.append(name)
            return print(f"You are in {name}")
        else:
            return print(f"Flight is full {name}")

    def seats_left(self) -> bool:
        return  self.capacity > len(self.passangers)
    

flights = Flight(5)
flights.add_passangers("John")
flights.add_passangers("Doe")
flights.add_passangers("Ava")
flights.add_passangers("Max")
flights.add_passangers("Adrina")
flights.add_passangers("Jack")
