from Recursion_Exercise import *

# fibonacci
def test_0():
    assert fibonacci(0) == 0

def test_1():
    assert fibonacci(1) == 1

def test_2():
    assert fibonacci(2) == 1

def test_3():
    assert fibonacci(3) == 2

def test_4():
    assert fibonacci(4) == 3

def test_5():
    assert fibonacci(5) == 5

def test_6():
    assert fibonacci(6) == 8

def test_7():
    assert fibonacci(7) == 13


# bunnyEars2
def test_0():
    assert bunnyEars2(0) == 0

def test_1():
    assert bunnyEars2(1) == 2

def test_2():
    assert bunnyEars2(2) == 5

def test_3():
    assert bunnyEars2(3) == 7

def test_4():
    assert bunnyEars2(4) == 10

def test_5():
    assert bunnyEars2(5) == 12

def test_6():
    assert bunnyEars2(6) == 15

def test_7():
    assert bunnyEars2(10) == 25


# triangle
def test_0():
    assert triangle(0) == 0

def test_1():
    assert triangle(1) == 1

def test_2():
    assert triangle(2) == 3

def test_3():
    assert triangle(3) == 6

def test_4():
    assert triangle(4) == 10

def test_5():
    assert triangle(5) == 15

def test_6():
    assert triangle(6) == 21

def test_7():
    assert triangle(7) == 28


# sumDigits
def test_0():
    assert sumDigits(126) == 9

def test_1():
    assert sumDigits(49) == 13

def test_2():
    assert sumDigits(12) == 3

def test_3():
    assert sumDigits(10) == 1

def test_4():
    assert sumDigits(1) == 1

def test_5():
    assert sumDigits(0) == 0

def test_6():
    assert sumDigits(730) == 10

def test_7():
    assert sumDigits(1111) == 4

def test_8():
    assert sumDigits(11111) == 5

def test_9():
    assert sumDigits(10110) == 3

# def test_10():
#     assert sumDigits(235) == 10


# change Pi
def test_0():
    assert changePi("xpix") == "x3.14x"

def test_1():
    assert changePi("pipi") == "3.143.14"

def test_2():
    assert changePi("pip") == "3.14p"

def test_3():
    assert changePi("pi") == "3.14"

def test_4():
    assert changePi("hip") == "hip"

def test_5():
    assert changePi("p") == "p"

def test_6():
    assert changePi("x") == "x"

def test_7():
    assert changePi("") == ""

def test_8():
    assert changePi("pixx") == "3.14xx"

def test_9():
    assert changePi("xyzzy") == "xyzzy"

# array6
def test_0():
    assert array6([1, 6, 4], 0) == True

def test_1():
    assert array6([1, 4], 0) == False

def test_2():
    assert array6([6], 0) == True

def test_3():
    assert array6([], 0) == False

def test_4():
    assert array6([6, 2, 2], 0) == True

def test_5():
    assert array6([2, 5], 0) == False

def test_6():
    assert array6([1, 9, 4, 6, 6], 0) == True

def test_7():
    assert array6([2, 5, 6], 0) == True

# noX
def test_0():
    assert noX("xaxb") == "ab"

def test_1():
    assert noX("abc") == "abc"

def test_2():
    assert noX("xx") == ""

def test_3():
    assert noX("") == ""

def test_4():
    assert noX("axxbxx") == "ab"

def test_5():
    assert noX("Hellox") == "Hello"

# stringClean
def test_0():
    assert stringClean("yyzzza") == "yza"

def test_1():
    assert stringClean("abbbcdd") == "abcd"

def test_2():
    assert stringClean("Hello") == "Helo"

def test_3():
    assert stringClean("XXabcYY") == "XabcY"

def test_4():
    assert stringClean("112ab445") == "12ab45"

def test_5():
    assert stringClean("Hello Bookkeeper") == "Helo Bokeper"

# strDist
def test_0():
    assert strDist("catcowcat", "cat") == 9

def test_1():
    assert strDist("catcowcat", "cow") == 3

def test_2():
    assert strDist("cccatcowcatxx", "cat") == 9

def test_3():
    assert strDist("abccatcowcatcatxyz", "cat") == 12

def test_4():
    assert strDist("xyx", "x") == 3

def test_5():
    assert strDist("xyx", "y") == 1

def test_6():
    assert strDist("xyx", "z") == 0

def test_7():
    assert strDist("z", "z") == 1

def test_8():
    assert strDist("x", "z") == 0

def test_9():
    assert strDist("", "z") == 0

def test_10():
    assert strDist("hiHellohihihi", "hi") == 13

def test_11():
    assert strDist("hiHellohihihi", "hih") == 5

def test_12():
    assert strDist("hiHellohihihi", "o") == 1

def test_13():
    assert strDist("hiHellohihihi", "ll") == 2