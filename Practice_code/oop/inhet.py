class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"
    

class Cow(Animal):
    pass


if __name__ == "__main__":
    dog = Dog("Buddy")
    print(dog.speak())  # Output: Buddy says Woof!

    cat = Cat("Whiskers")
    print(cat.speak())  # Output: Whiskers says Meow!

    bird = Bird("Tweetie")
    print(bird.speak())  # Output: Tweetie says Chirp!

    cow = Cow("Mohh")
    print(cow.speak())  # Output: Tweetie says Chirp!
