import math


# test sum(numbers: List[float]) -> float
def test_sum():
    assert sum([]) == 0
    assert sum([1, 2, 3]) == 6
    assert sum([1] * 1000) == 1000


# test math.ceil(float) -> int
def test_math_ceil():
    assert math.ceil(4.9) == 5

# test math.floor(float) -> int
def test_math_floor():
    assert math.floor(4.1) == 4

# test f strings
def test_f_strings():
    a = 5
    assert f"hello{a}" == "hello5"

# test .format()
# def test_format():
    # assert 