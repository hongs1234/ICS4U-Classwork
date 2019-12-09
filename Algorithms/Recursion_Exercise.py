# Fibonacci
def fibonacci(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    return fibonacci(num-1) + fibonacci(num-2)

# Triangle


# sumDigits
# def sumDigits()

# Allstar
# def allStar(word: str):


# bunnyEars2
def bunnyEars2(n: int):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 3 + bunnyEars2(n-1)
    else:
        return 2 + bunnyEars2(n-1)

# triangle
def triangle(n: int):
    if n == 0:
        return 0
    return n + triangle(n-1)


# sumDigits
def sumDigits(n: int):
    if n == 0:
        return 0
    right_most = n % 10
    n = n/10
    return right_most + sumDigits(n)

# changePi
def changePi(word: str):
    n = len(word) - 1
    if n == 1:
        return word[n]
    if word[n-1] + word[n] == "pi":
        return "3.14" + changePi(n-1)
    else:
        return word[n] + changePi(n-1)


# noX
# def noX(word: str):
#     n = 0
#     if n == word[-1]:
#         return word
#     if word[n] == "x":
#         return noX(word[n+1:])
#     else:
#         return noX(word[n:])


# array6
def array6(nums: List[int], n: int):
    if n > len(nums):
        return False
    if num[n] == 6:
        return True
    else:
        return array6(nums, n + 1)