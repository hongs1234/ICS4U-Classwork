"""
INHERITANCE
"""

class Dog:
    """Dog Class
    
    Attributes:
        name: str
        breed: str
    """

    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
    
    def __str__(self):
        return f"{self.name}"

    def make_sound(self):
        pass


class Squirrel:
    """Squirrel Class
    
    Attributes:
        name: str
        nuts_collected: int
    """

    def __init__(self, name: str, nuts_collected: int):
        self.name = name
        self. nuts_collected = nuts_collected
    
    def __str__(self):
        return f"{self.name}"
    
    def make_sound(self):
        pass