from typing import List

class Pizza:
    """Pizza Class
    
    Attributes:
        name: str
        toppings: List[str]
    """

    num_pizzas = 0

    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings
        self.id = Pizza.num_pizzas
        Pizza.num_pizzas += 1
    
    def __str__(self):
        return f"{self.name}, id: {self.id}, toppings: {self.toppings}"

    @classmethod
    def pepperoni(cls) -> "Pizza":
        new_pizza = cls("Pepperoni", ["cheese", "pepperoni"])
        return new_pizza

    def hawaiian(cls) -> "Pizza":
        return cls("Hawaiian", ["pepperoni", "cheese", "pineapple"])

    def cheese(cls) -> "Pizza":
        return cls("Cheese", ["cheese"])

    def search_by_name(cls, name: str):
        




def main():
    pizza1 = Pizza.hawaiian()
    pizza2 = Pizza.pepperoni()
    pizza3 = Pizza.cheese()

    print(pizza1)
    print(pizza2)
    print(pizza3)

if __name__ == "__main__":
    main()