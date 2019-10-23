class Food:
    """Food Class
    
    Attributes:
        name(str): food name
        cost(int): price of food
        nutrition(int): nutritious value of food
    """

    def __init__(self, name: str, cost: int, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition


class Dog:
    """Dog Class
    
    Attirbutes:
        name: str
        breed: str
        happiness: int

    Methods:
        __str__: str
        eat(Food): void
        bark(): void
    """
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
        self.happiness = 100

    def __str__(self) -> str:
        return f"{self.name}, happiness: {self.happiness}"

    def bark(self):
        print("RUFF RUFF!")

    def eat(self, food: Food):
        happiness_increase = food.nutrition / 10
        self.happiness += happiness_increase


def main():
    dog = Dog("Jah", "poodle")
    print(dog)

    dog.bark()
    apple = Food("Apple", 1, 10)
    dog.eat(apple)

    print(dog)


if __name__ == "__main__":
    main()
