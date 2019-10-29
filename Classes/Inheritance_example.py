"""
INHERITANCE
"""

class Animal:
    sound = "Generic sound"

    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

    @classmethod
    def make_sound(cls):
        print(cls.sound)


class Dog(Animal):
    """Dog Class
    
    Attributes:
        name: str
        breed: str
    """
    sound = "WOOF"

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed


class Squirrel(Animal):
    """Squirrel Class
    
    Attributes:
        name: str
        nuts_collected: int = 0
    """
    sound = "SQUEEK"


class Cat(Animal):
    sound = "MEOW"


def main():
    dog = Dog("Rover", "Poodle")
    squirrel = Squirrel("Sammy")
    cat = Cat("Tila")

    dog.make_sound()
    squirrel.make_sound()
    cat.make_sound()

    print(dog)
    print(squirrel)
    print(cat)


if __name__ == "__main__":
    main()