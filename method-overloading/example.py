# Method Overloading
import random


def draw_circle(x, y, radius=None):
    if radius is None:
        random.randrange(100)
    print(f"Drawing circle at {x}, {y} with radius of {radius}")


draw_circle(100, 100)
draw_circle(200, 200)
draw_circle(300, 300, 70)