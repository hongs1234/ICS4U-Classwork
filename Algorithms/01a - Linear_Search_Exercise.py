from typing import List


def find_num(target: int, numbers: List[int]) -> int:
    """Find target number from list of ints
    
    Arg:
        target: value to find
        numbers: list of numbers
    Returns:
        Index of target number. -1 if not found
    """
    
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1


def last_occurance(target: int, numbers: List[int]) -> int:
    """Find the last occurance of a number from a list of ints
    
    Arg:
        target: value to find
        numbers: list of numbers
    Returns:
        Index of the last occurance of the target number. -1 if not found.
    """

    pass
# len - 1 - i

def every_occurance(target: int, numbers: List[int]) -> List:
    """Find every occurance of a number from a list
    
    Arg:
        target: value to find
        numbers: list of numbers
    Returns:
        A list of indexes where the target occurs. An empty list if not found
    """

    pass


def first_string_occurance(target: str, words: List[str]) -> int:
    """Find the first occurance that a string begins with a substring
    
    Arg:
        target: substring to find
        words: list of words
    Returns:
        Index of the first word that begins with the target substring
    """

    pass


def all_words(target: str, words: List[str]) -> List:
    """Find all the words that begin with a substring
    
    Arg:
        target: substring to find
        words: list of words
    Returns:
        List of all the words beginning with the target substring
    """

    pass

 
# TESTS
def test_find_num():
    assert find_num(3, []) == -1
    assert find_num(3, [3, 6, 5]) == 0
    assert find_num(3, [2, 5, 9, 3]) == 3
    assert find_num(3,[2, 3, 5, 3]) == 1


def test_last_occurance():
    assert last_occurance(2, []) == -1
    assert last_occurance(2, [2, 3, 1]) == 0
    assert last_occurance(2, [9, 2, 4, 6, 2]) == 4


def test_every_occurance():
    assert every_occurance(4, []) == []
    assert every_occurance(4, [1, 4, 2]) == [1]
    assert every_occurance(4, [4, 5, 2, 4, 4]) == [0, 3, 4]


def test_first_string_occurance():
    assert first_string_occurance("in", []) == -1
    assert first_string_occurance("in", ["outside", "inside"]) == 1
    assert first_string_occurance("in", ["ink", "here"]) == 0
    assert first_string_occurance("in", ["there", "intake", "innuendo"]) == 1


def test_all_words():
    assert all_words("he", []) == []
    assert all_words("he", ["here", "jokes"]) == ["here"]
    assert all_words("he", ["crude", "hello", "oil", "help"]) == ["hello", "help"]