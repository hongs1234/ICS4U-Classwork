# Q1
class Food:
    def __init__(self, name: str, cost: int, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

food = Food("Bread", 4, 10)

#Q2
class Dog:
    def __init__(self, name: str, breed: str, happiness: int):
        self.name = name
        self. breed = breed
        self.happiness = happiness
    
    def eat(self, food):
        self.happiness += int((food.nutrition * 0.1))

    def bark():
        print("RUFF RUFF!")

    def __str__():
        print(f"""Name: {name}
        Happiness: {happiness}""")

food = Food("Bread", 6, 10)
dog = Dog("Jok", "Dalmation", 5)
