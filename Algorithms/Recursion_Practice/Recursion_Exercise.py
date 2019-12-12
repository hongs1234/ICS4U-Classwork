from typing import List

# 01-factorial
def factorial(n: int):
    if n == 1:
        return 1
    return n * factorial(n-1)

# 02-bunnyEars
def bunnyEars(n:int):
    if n == 0:
        return 0
    return 2 + bunnyEars(n-1)

# 03-Fibonacci
def fibonacci(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    return fibonacci(num-1) + fibonacci(num-2)

# 04-bunnyEars2
def bunnyEars2(n: int):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 3 + bunnyEars2(n-1)
    else:
        return 2 + bunnyEars2(n-1)

# 05-triangle
def triangle(n: int):
    if n == 0:
        return 0
    return n + triangle(n-1)


# 06-sumDigits
def sumDigits(n: int):
    if n == 0:
        return 0
    right_most = n % 10
    return right_most + sumDigits(n/10)

# 07-count7
def count7(n: int):
    if n == 0:
        return 0
    right_most = n % 10
    if right_most == 7:
        return 1 + count7(n//10)
    return count7(n//10)

# 08-count8
def count8(n: int):
    if n == 0:
        return 0
    right_most = n % 10
    last_two = n % 100
    if last_two == 88:
        return 2 + count8(n//10)
    elif right_most == 8:
        return 1 + count8(n//10)
    return count8(n//10)

# 09-powerN

# 10-countX

# 11-countHi

# 12-changeXY 

# 13-changePi
def changePi(word: str):
    if len(word) == 0:
        return ""
    if word[:2] == "pi":
        return "3.14" + changePi(word[2:])
    return word[0] + changePi(word[1:])

# 14-noX
def noX(word: str):
    if len(word) < 1:
        return ""
    a = word[0]
    if a == "x":
        return noX(word[1:])
    return a + noX(word[1:])

# 15-array6
def array6(nums: List[int], n: int):
    if len(nums) == n:
        return 0
    return nums[n] == 6 or array6(nums, n + 1)

# 16-array11

# 17-array220

# 18-Allstar
# def allStar(word: str):

# 19-pairStar

# 20-endX

# 21-countPairs

# 22-countABC

# 23-count11

# 24-stringClean
def stringClean(word: str):
    if len(word) <= 1:
        return word
    a = word[0]
    b = word[1]
    if a == b:
        return stringClean(word[1:])
    return a + stringClean(word[1:])

# 25-countHi2

# 26-parenBit

# 27-nestParen

# 28-strCount

# 29-strCopies

# 30-strDist
def strDist(word: str, substring: str):
    if len(word) < len(substring):
        return 0
    if word.startswith(substring) and word.endswith(substring):
        return len(word)
    if word.startswith(substring):
        return strDist(word[:-1], substring)
    return strDist(word[1:], substring)