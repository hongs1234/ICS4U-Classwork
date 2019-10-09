# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age


# people = [
#     Person("Jeff", 35),
#     Person("Sally", 43),
#     Person("Jim", 32),
#     Person("Frank", 65)
# ]

# print(people[1].name)

class Person:
    def __init__(self):
        print("Create new person")

a = Person()
b = a

print(a)
print(b)

del a

print(b)


