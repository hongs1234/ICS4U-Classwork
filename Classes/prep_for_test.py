# Q1
class Food:
    """Food Class
    
    Attributes:
        name(str): the name of the food
        cost(int): how much the food costs
        nutrition(int): """
    def __init__(self, name: str, cost: int, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

food = Food("Bread", 4, 10)

#Q2
class Dog:
    """Dog Class
    
    Attributes:
        name(str): name of the dog
        breed(str): breed of dog
        happiness(int): happiness level of dog
    """
    
    def __init__(self, name: str, breed: str):
        self.name = name
        self. breed = breed
        self.happiness = 100
    
    def eat(self, food):
        self.happiness += int((food.nutrition * 0.1))

    def bark():
        print("RUFF RUFF!")

    def __str__():
        print(f"""Name: {name}
        Happiness: {happiness}""")

food = Food("Bread", 6, 10)
dog = Dog("Jok", "Dalmation", 5)

print(dog.__str__)