from typing import List

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
    return right_most + sumDigits(n/10)

# changePi
def changePi(word: str):
    if len(word) == 0:
        return ""
    if word[:2] == "pi":
        return "3.14" + changePi(word[2:])
    return word[0] + changePi(word[1:])


# noX
def noX(word: str):
    if len(word) <= 1:
        return ""
    a = word[0]
    if a == "x":
        return noX(word[1:])
    return a + noX(word[1:])


# array6
def array6(nums: List[int], n: int):
    if len(nums) == n:
        return 0
    return nums[n] == 6 or array6(nums, n + 1)

# stringClean
def stringClean(word: str):
    if len(word) <= 1:
        return word
    a = word[0]
    b = word[1]
    if a == b:
        return stringClean(word[1:])
    return a + stringClean(word[1:])

# strDist
def strDist(word: str, substring: str):
    if len(word) < len(substring):
        return 0
    if word.startswith(substring) and word.endswith(substring):
        return len(word)
    if word.startswith(substring):
        return strDist(word[:-1], substring)
    return strDist(word[1:], substring)