class Person:
    def __init__(self, name: str, height: int, strength: int):
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = 100
    
    def __str__(self):
        return f"{self.name}, hp: {self.health_points}"
    
    def introduce(self):
        print(f"Hello, my name is {self.name}")
    
    def punch(self, person):
        print(f"{self.name} punched {person.name}")
        if self == person:
            person.health_points -= 2
        else:
            person.health_points -= (self.strength * 2)
    
    def eat(self):
        print(f"{self.name} ate")
        self.health_points = 100


Jin = Person("Jin", 170, 1)
Marly = Person("Marly", 165, 2)

Jin.introduce()
Marly.introduce()

for x in range(10):
    Jin.punch(Jin)

Jin.eat()

print(Jin)
print(Marly)