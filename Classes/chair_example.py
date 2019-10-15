class Person:
    pass

class Chair:
    """
    Attributes:
        colour: str
        num_legs: int
        height: int
        occupant: Object
    """
    
    def __init__(self, colour: str, num_legs: int, height: int):
        self.colour = colour
        self.num_legs = num_legs
        self.height = height
        self.occupant = None

c1 = Chair("green", 4, 75)
c2 = Chair("bluee", 4, 75)

c1.occupant = Person()

print(c1.occupant)
