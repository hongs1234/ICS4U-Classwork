from typing import List


# Linear Search
# 1. Basic linear search
# 2. Get last occurance of value
# 3. Get list of all occurances


def linear_search(target: int, numbers: List[int]) -> int:
    """Search for target number in a list of numbers.
    
    Arg:
        target: the value to find
        numbers: the list to search
    Returns:
        Index location of the found target number. -1 for not found.
    """

    for i, num in enumerate(numbers):
        if num == target:
            return i
    
    return -1


def test_linear_search():
    assert linear_search(5, []) == -1
    assert linear_search(5, [5, 8]) == 0
    assert linear_search(5, [1, 2, 3, 5]) == 3
    assert linear_search(5, [4, 7, 5, 5, 3]) == 2